import os
import requests
from dotenv import load_dotenv

load_dotenv()

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets/v2"

HEADERS = {
    "APCA-API-KEY-ID": ALPACA_API_KEY,
    "APCA-API-SECRET-KEY": ALPACA_SECRET_KEY,
    "accept": "application/json"
}

def get_alpaca_account():
    url = f"{BASE_URL}/account"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_alpaca_positions():
    url = f"{BASE_URL}/positions"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_normalized_portfolio():
  positions = get_alpaca_positions()
  normalized_data = []
  
  for pos in positions:
    normalized_data.append({
      "asset": pos.get("symbol"),
      "asset_type":"stock",
      "quantity": float(pos.get("qty")),
      "total_value": float(pos.get("market_value"))

    })
    return normalized_data
if __name__ == "__main__":
    account = get_alpaca_account()
    print(f"Total Equity: ${account.get('equity')}")
    print(f"Buying Power: ${account.get('buying_power')}")
    print("-" * 20)
    
    positions = get_alpaca_positions()
    for position in positions:
        symbol = position.get('symbol')
        qty = position.get('qty')
        value = position.get('market_value')
        print(f"{symbol}: {qty} shares | Value: ${value}")