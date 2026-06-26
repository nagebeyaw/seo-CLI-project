import os
import requests 
from dotenv import load_dotenv

client_api = "9DuVKqEsHc4VLRAAW5z6I2DvgkXiKvT3"
BASE_URL = f"https://api.developer.coinbase.com/rpc/v1/base/{client_api}"
Wallet_ADDRESS = "0xec0E36a6060339694C618ffFfcC9eC7da21Cb0CC"
headers = {
  "Content-Type": "application/json"
}

def get_coinbase_balance():
  response = requests.post(
    BASE_URL,
    headers = headers,
    json = {
      "jsonrpc": "2.0",
      "id": 1,
      "method": "cdp_listBalances",
      "params": [{
        "address": Wallet_ADDRESS,
        "pageToken":"",
        "pageSize": 2
      }]
    }
  )
  return response.json()

symbols = {
  "005a8364-a0c4-5df8-b9f3-726fb286986b":"Wrapped Ether",
  "0e6607fc-adf7-53a8-a353-dc411a70e9c1": "USDC Coin"
}


def normalize_asset(asset):
  asset_info = asset.get("asset")
  qty = asset.get("value")
  real_qty = qty /(10**18)
  return {
    "asset": asset_info.get("id"),
    "quantity": real_qty,
  }

def get_portfolio():
  data = get_coinbase_balance()
  #print(data)
  if data.get('result').get('balances') != None:
    fixed_data = data.get('result').get('balances')
    output = []
    for item in fixed_data:
      output.append(normalize_asset(item))
    return output
  print("data is NONE")
  return []
  

if __name__ == "__main__":
  crypto = get_portfolio()
  if crypto == None:
    print("No crypto assets owned.")
  else:
    for item in crypto:
      asset = item.get("asset")
      qty = item.get("quantity")
      symbol_name = symbols.get(asset)
      if symbol_name == 'Wrapped Ether':
        price = 1564
      else:
        price = 1
      cost = qty * price
      print(f"Asset: {symbol_name} | Type: Crypto | Quantity: {qty:.3f} | Worth: ${cost:.3f}")
