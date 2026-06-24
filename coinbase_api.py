import os
import requests 
from cdp.auth.utils.jwt import generate_jwt, JwtOptions
from dotenv import load_dotenv

load_dotenv()


api_coinbase =  os.getenv("C_API_KEY")
private_coinbase = os.getenv("C_PRIVATE_KEY")

jwt_token = generate_jwt(JwtOptions(
  api_key_id = api_coinbase,
  api_key_secret = private_coinbase,
  request_method = "GET",
  request_host = "api.cdp.coinbase.com",
  request_path = "/platform/v2/accounts",
  expires_in =120
))

URL ="https://api.cdp.coinbase.com/platform/v2/accounts"
response = requests.get(
  URL,
  headers = {"Authorization": f"Bearer {jwt_token}", "Content-Type": "application/json"
  }
)

#client_api = "9DuVKqEsHc4VLRAAW5z6I2DvgkXiKvT3"
#URL = f"https://api.developer.coinbase.com/rpc/v1/base/{client_api}"


#response = requests.post(
#  URL, 
#  headers = {"Content-Type" : "application/json"},
#  json = {"jsonrpc": "2.0", "id":1, "method": "cdp_listBalances", "params": [{"address":"0x887B9075c779407c931F9dE7Bc14e5d3c4DB2417"}]
#  }
#)


print(response.text)

print(response.status_code)
#response_data = response.json()
