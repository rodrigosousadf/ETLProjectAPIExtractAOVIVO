import requests

url = 'https://api.coinbase.com/v2/prices/spot'

headers = {
    'Accept': 'application/json',
    'user-agent': 'MinhaAplicacao/1.0"
}
params = {"currency": "USD"} # moeda da consulta

data = requests.get(url, headers=headers, params=params)
print("Preço do Bitcoin em USD:", data.json()['data']['amount'])
