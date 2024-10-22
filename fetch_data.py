# fetch_data.py

import requests
from config import headers

def fetch_crypto_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    params = {
        'start': '1',
        'limit': '10',
        'convert': 'USD'
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data['data']
