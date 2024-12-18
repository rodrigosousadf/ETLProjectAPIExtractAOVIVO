import time
import requests
from tinydb import TinyDB
import datetime 

def obter_preco_bitcoin():
    url = "https://api.coinbase.com/v2/prices/BTC-USD/spot"
    response = requests.get(url)
    dados = response.json()
    return dados['data']

def transformar_dados(dados):
    valor = dados["amount"]
    criptomoeda = dados["base"]
    moeda = dados["currency"]
    timestamp = datetime.datetime.now().timestamp()
    transformar_dados = {
        'valor': valor,
        'criptomoeda': criptomoeda,
        'moeda': moeda,
        'timestamp': timestamp
    }

    return transformar_dados

def salva_dados_tinydb(dados, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos com sucesso!")

if __name__ == "__main__":
    while True:
        # Obtém os dados da API
        dados_bitcoin = obter_preco_bitcoin()
        
        # Transforma os dados
        dados_transformados = transformar_dados(dados_bitcoin)

        # Salva os dados no banco de dados
        salva_dados_tinydb(dados_transformados)

        # Aguarda 15 segundos antes de obter novos dados
        time.sleep(15)
