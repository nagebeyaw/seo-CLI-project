import os
import requests 
from dotenv import load_dotenv
from coinbase.rest import RESTClient

load_dotenv()


# key_coinbase =  os.getenv("C_API_KEY")
# private_coinbase = os.getenv("C_PRIVATE_KEY")

# client = RESTClient(
#   api_key:key_coinbase,
#   api_secret : private_coinbase,
#   base_url : "api-public.sandbox.exchange.coinbase.com",
#   sandbox:True

#)
#print (client.get_product("BTC-USD"))
#print(client.get_accounts())



#print()

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
  # Can do some test coinbase
  return response.json()

symbols = {
  "005a8364-a0c4-5df8-b9f3-726fb286986b":"Wrapped Ether",
  "0e6607fc-adf7-53a8-a353-dc411a70e9c1": "USDC Coin"

}
# def symbols_for_tokens(token):
#   if token in symbols:
#     return symbols[token]
#   else:
#     url_symbol = "https://api,etherscan.io/api"
    



def normalize_asset(asset):
  asset_info = asset.get("asset")
  qty = asset.get("value")
  real_qty = qty /(10**18)
  return {
    "asset": asset_info.get("id"),
    "quantity": real_qty,
    "total_value": 0.0
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
  print("data is NONe")
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
      print(f"Asset: {symbol_name} | Type: Crypto | Quantity:{qty:.3f}")

# response = requests.post(
#   URL, 
#   headers = {"Content-Type" : "application/json"},
#   json = {"jsonrpc": "2.0", "id":1, "method": "cdp_listBalances", "params": [{"address":"0x887B9075c779407c931F9dE7Bc14e5d3c4DB2417"}],
#   "pageToken" : "", "pageSize" :10
#   }
# )




# print(response.text)

# print(response.status_code)
# response_data = response.json()
