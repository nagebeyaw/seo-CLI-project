import os 
import requests
import json 
from dotenv import load_dotenv

load_dotenv()
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets/v2"

HEADERS = {
  "APCA-API-KEY-ID": os.getenv("ALPACA_API_KEY"),
  "APCA-API-SECRET-KEY": os.getenv("ALPACA_SECRET_KEY"),
  "accept": "application/json"

}
def get_alpaca_positions():
  url = f"{BASE_URL}/positions"
  response = requests.get(url, headers=HEADERS)
  response.raise_for_status()
  return response.json()

def get_normalized_portfolio():
  positions = get_alpaca_positions()
  if positions is None:
    positions = []
  normalized_data = []
  for pos in positions:
    normalized_data.append({
      "asset": pos.get("symbol"),
      "asset_type": "stock",
      "quantity": float(pos.get("qty", 0)),
      "total_value": float(pos.get("market_value", 0))
        })
  return normalized_data

def get_coinbase_positions():
  client_api = os.getenv("COINBASE_API_KEY")
  url = f"https://api.developer.coinbase.com/rpc/v1/base/{client_api}"
  payload = {
    "jsonrpc": "2.0", 
    "id": 1, 
    "method": "cdp_listBalances", 
    "params": [{
    "address": "0x887B9075c779407c931F9dE7Bc14e5d3c4DB2417",
    "pageToken": "", 
    "pageSize": 10
        }]
  }
  response = requests.post(
    url, 
    headers={"Content-Type": "application/json"}, 
    json=payload
  )
  response.raise_for_status()
  return response.json()

def get_normalized_crypto():
  balances = []

  data = get_coinbase_positions()

  if data and isinstance(data, dict):
    result_dict = data.get("result", {})
    if result_dict and isinstance(result_dict, dict):
      extracted_balances = result_dict.get("balances", [])
      # Final check in case Coinbase explicitly returned null
      if extracted_balances is not None:
        balances = extracted_balances



  normalized_data = []

  for pos in balances:
    asset_info = pos.get("asset", {})
    symbol = asset_info.get("symbol", "CRYPTO") if isinstance(asset_info, dict) else str(pos.get("asset","CRYPTO"))

    normalized_data.append({
        "asset": symbol,
        "asset_type": "crypto",
        "quantity": float(pos.get("amount", 0 )),
        "total_value": float(pos.get("value", 0))
      })
  return normalized_data

def get_total_portfolio():
  stock_data = get_normalized_portfolio()
  crypto_data = get_normalized_crypto()
  return stock_data + crypto_data

if __name__ == "__main__":
  portfolio = get_total_portfolio()
  print(json.dumps(portfolio, indent=4))