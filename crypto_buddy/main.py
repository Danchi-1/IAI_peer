# main.py - CryptoBuddy Cryptocurrency Advisor
# ----------------------------------------------------
# This script fetches real-time cryptocurrency data, updates energy usage values,
# validates crypto data, and exports structured results in JSON and CSV formats.
# ----------------------------------------------------

import requests
import json
import csv
import os
from data_validator import update_crypto_energy_data, validate_crypto_db

# Load API key securely from environment variables instead of hardcoding
API_KEY = os.getenv('COINMARKETCAP_API_KEY')
if not API_KEY:
    raise ValueError("Missing API key. Set COINMARKETCAP_API_KEY as an environment variable.")

# CoinMarketCap API URL for retrieving crypto listings
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# API Request Headers
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

# API Query Parameters - Retrieves top 10 cryptocurrencies
params = {
    'start': '1',
    'limit': '10',
    'convert': 'USD'
}

def get_sustainability_score(symbol):
    """Assign sustainability scores based on external research and eco-friendliness."""
    sustainability_scores = {
        'BTC': 40,
        'ETH': 60,
        'ADA': 85,
        'SOL': 80,
        'XRP': 70
    }
    return sustainability_scores.get(symbol.upper(), 60)  # Default to 60 if not listed

def fetch_crypto_data():
    """Fetch real-time cryptocurrency data from CoinMarketCap API."""
    try:
        response = requests.get(URL, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
        return None  # Return None to indicate failure

def process_crypto_data():
    """Process API data and generate a structured crypto database."""
    data = fetch_crypto_data()
    if not data or 'data' not in data:
        print("⚠️ Failed to retrieve cryptocurrency data.")
        return {}

    crypto_db = {}

    for coin in data['data']:
        symbol = coin['symbol']
        crypto_db[symbol] = {
            'name': coin['name'],
            'symbol': symbol,
            'market_cap': coin['quote']['USD']['market_cap'],
            'price': coin['quote']['USD']['price'],
            'energy_usage_mwh_per_day': None,  # Placeholder for energy data
            'sustainability_score': get_sustainability_score(symbol)
        }

    # Update energy usage estimates
    crypto_db = update_crypto_energy_data(crypto_db)
    return crypto_db

def save_json(data, filename="crypto_db.json"):
    """Save cryptocurrency data as a formatted JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"✅ JSON data saved to {filename}")