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
URL = f"https://api.developer.coinbase.com/rpc/v1/base/{client_api}"


response = requests.post(
  URL, 
  headers = {"Content-Type" : "application/json"},
  json = {"jsonrpc": "2.0", "id":1, "method": "cdp_listBalances", "params": [{"address":"0x887B9075c779407c931F9dE7Bc14e5d3c4DB2417"}],
  "pageToken" : "", "pageSize" :10
  }
)




print(response.text)

print(response.status_code)
response_data = response.json()
