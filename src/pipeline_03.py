import os
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

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

# Monta a URL de conexão ao banco PostgreSQL (sem ?sslmode=...)
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    print("Tabela criada/verificada com sucesso!")

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    try:
        resposta = requests.get(url, timeout=10)  # Adiciona timeout
        resposta.raise_for_status()  # Levanta exceção para status codes não-200
        return resposta.json()
    except requests.RequestException as e:
        logging.error(f"Erro ao acessar a API: {e}")
        return None

def tratar_dados_bitcoin(dados_json):
    """Transforma os dados brutos da API e adiciona timestamp."""
    if not dados_json or 'data' not in dados_json:
        logging.error("Dados JSON inválidos")
        return None
    
    try:
        valor = float(dados_json['data']['amount'])
        criptomoeda = dados_json['data']['base']
        moeda = dados_json['data']['currency']
        timestamp = datetime.now()
        
        dados_tratados = {
            "valor": valor,
            "criptomoeda": criptomoeda,
            "moeda": moeda,
            "timestamp": timestamp
        }
        return dados_tratados
    except (KeyError, ValueError) as e:
        logging.error(f"Erro ao tratar dados: {e}")
        return None

def salvar_dados_postgres(dados):
    """Salva os dados no banco PostgreSQL."""
    if not dados:
        logging.error("Dados inválidos para salvar")
        return

    try:
        with Session() as session:  # Usa context manager
            novo_registro = BitcoinPreco(**dados)
            session.add(novo_registro)
            session.commit()
            logging.info(f"Dados salvos no PostgreSQL: {dados['timestamp']}")
    except Exception as e:
        logging.error(f"Erro ao salvar no banco de dados: {e}")

if __name__ == "__main__":
    criar_tabela()
    logging.info("Iniciando ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")

    while True:
        try:
            dados_json = extrair_dados_bitcoin()
            if dados_json:
                dados_tratados = tratar_dados_bitcoin(dados_json)
                if dados_tratados:
                    salvar_dados_postgres(dados_tratados)
            time.sleep(15)
        except KeyboardInterrupt:
            logging.info("\nProcesso interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            logging.error(f"Erro durante a execução: {e}")
            time.sleep(15)