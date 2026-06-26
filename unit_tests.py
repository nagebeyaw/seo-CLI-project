import unittest 
from unittest.mock import patch
from api_manager import get_normalized_portfolio
from api_manager import get_normalized_crypto

class Test_portfolio_Functions(unittest.TestCase):
  @patch('api_manager.get_coinbase_positions')
  def test_get_normalized_crypto(self, mock_crypto):
    mock_crypto.return_value = {
      "result": {"balances":[{"asset": {"symbol": "BTC"}, "amount": "0.5", "value": "25000"}]}
    }
    result = get_normalized_crypto()
    self.assertEqual(result[0]["asset"],"BTC")

  @patch('api_manager.get_alpaca_positions')
  def test_get_normalized_stocks(self, mock_positions):
    mock_positions.return_value = [
      {"symbol": "AAPL", "qty":"10.5", "market_value":1500.00}
    ]
    result = get_normalized_portfolio()
    self.assertEqual(result[0]["asset"], "AAPL")
    self.assertEqual(result[0]["quantity"], 10.5)

  @patch('api_manager.get_alpaca_positions')
  def test_normalized_alpaca_empty(self, mock_positions):
    mock_positions.return_value  = [
    ]
    result = get_normalized_portfolio()
    self.assertEqual(result,[])
  @patch('api_manager.get_coinbase_positions')
  def test_normalized_crypto_empty(self,mock_crypto):
    mock_crypto.return_value=[]
    result = get_normalized_crypto()
    self.assertEqual(result,[])

if __name__ == "__main__":
  unittest.main()