import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Integração com Logfire
import logging
import logfire
from logging import basicConfig, getLogger

# Configura o Logfire e adiciona o handler
logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = getLogger(__name__)
logger.setLevel(logging.INFO)

# Importar Base e BitcoinPreco do database.py
from database import Base, BitcoinPreco

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")
PORT = int(os.getenv('PORT', 10000))  # Nova configuração de porta para o Render

# Constantes de configuração
SLEEP_TIME = 15  # segundos
API_URL = 'https://api.coinbase.com/v2/prices/spot'

# Configuração do banco de dados
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    logger.info("Tabela criada/verificada com sucesso!")

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase."""
    try:
        resposta = requests.get(API_URL, timeout=10)  # Adiciona timeout
        resposta.raise_for_status()  # Levanta exceção para status codes ruins
        return resposta.json()
    except requests.RequestException as e:
        logger.error(f"Erro na requisição à API: {e}")
        return None

def tratar_dados_bitcoin(dados_json):
    """Transforma os dados brutos da API e adiciona timestamp."""
    try:
        valor = float(dados_json['data']['amount'])
        criptomoeda = dados_json['data']['base']
        moeda = dados_json['data']['currency']
        timestamp = datetime.now()
        
        return {
            "valor": valor,
            "criptomoeda": criptomoeda,
            "moeda": moeda,
            "timestamp": timestamp
        }
    except (KeyError, ValueError) as e:
        logger.error(f"Erro ao tratar dados: {e}")
        return None

def salvar_dados_postgres(dados):
    """Salva os dados no banco PostgreSQL."""
    if not dados:
        logger.error("Dados inválidos para salvamento")
        return False
        
    session = Session()
    try:
        novo_registro = BitcoinPreco(**dados)
        session.add(novo_registro)
        session.commit()
        logger.info(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")
        return True
    except Exception as ex:
        logger.error(f"Erro ao inserir dados no PostgreSQL: {ex}")
        session.rollback()
        return False
    finally:
        session.close()

# Adiciona uma função simples para indicar que o serviço está rodando
def health_check():
    """Retorna uma mensagem indicando que o serviço está rodando."""
    return "ETL Service is running"

if __name__ == "__main__":
    logger.info(f"Iniciando servidor na porta {PORT}")
    criar_tabela()
    logger.info(f"Iniciando ETL com atualização a cada {SLEEP_TIME} segundos... (CTRL+C para interromper)")

    # Opcional: Adicionar um servidor web simples para responder a health checks
    from flask import Flask
    app = Flask(__name__)

    @app.route('/health')
    def health():
        return health_check()

    # Inicia o servidor Flask em uma thread separada
    from threading import Thread
    Thread(target=lambda: app.run(host='0.0.0.0', port=PORT, debug=False, use_reloader=False)).start()

    while True:
        try:
            dados_json = extrair_dados_bitcoin()
            if dados_json:
                dados_tratados = tratar_dados_bitcoin(dados_json)
                if dados_tratados:
                    sucesso = salvar_dados_postgres(dados_tratados)
                    if not sucesso:
                        logger.warning("Falha ao salvar dados")
            time.sleep(SLEEP_TIME)
        except KeyboardInterrupt:
            logger.info("Processo interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            logger.error(f"Erro não tratado durante a execução: {e}")
            time.sleep(SLEEP_TIME)