import os
import requests
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

def get_goal_amount(goal_name):
    goals = {
        "tuition": 40000.00,
        "rent": 1500.00,
        "car": 8000.00
    }
    return goals.get(goal_name.lower(), 0.0)

def calculate_goal_progress(current_equity, goal_amount):
    if goal_amount <= 0:
        return 0.0
    return (current_equity / goal_amount) * 100
#account endpoint to pull total equity and buying power,
#positions endpoint to print out the exact shares and live market values I currently hold.

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

total_equity = float(account.get('equity'))
print("-" * 20)
    
user_goal = input("Enter the name of your financial goal (e.g., tuition, laptop, vacation): ")
    
amount_input = input(f"Enter the dollar amount needed for {user_goal}: $")
    
try:
  target_amount = float(amount_input.replace(',', ''))
except ValueError:
  target_amount = 0.0
    
if target_amount > 0:
  percentage = calculate_goal_progress(total_equity, target_amount)
  remaining = max(0.0, target_amount - total_equity)
        
  print(f"\nGoal: {user_goal.capitalize()}")
  print(f"Target Amount: ${target_amount:,.2f}")
  print(f"Current Progress: {percentage:.2f}%")
  print(f"Remaining Needed: ${remaining:,.2f}")
else:
  print("\nInvalid amount entered. Please run again and enter a number (e.g., 1500).")