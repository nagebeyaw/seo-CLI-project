import database
from api_manager import get_total_portfolio
def calculate_goal_progress(current_equity, goal_amount):
    if goal_amount <= 0:
        return 0.0
    return (current_equity / goal_amount) * 100
def display_portfolio(portfolio_data):
  print("\n" + "="*40)
  print("          CURRENT PORTFOLIO")
  print("="*40)
    
  total_value = 0.0
  stock_value = 0
  crypto_value = 0.0

  other branch version

  for item in portfolio_data:
    asset = item.get('asset', 'UNKNOWN')
    qty = float(item.get('quantity', 0))
    val = float(item.get('total_value', 0))
    a_type = item.get('asset_type', 'unknown').upper()
        
    total_value += val
    if a_type == 'STOCK':
      stock_value += val
    elif a_type == 'CRYPTO':
      crypto_value += val
    print(f"[{a_type}] {asset:<8} | QTY: {qty:<10.4f} | VAL: ${val:,.2f}")
        
  print("-" * 40)
  print(f"TOTAL NET WORTH: ${total_value:,.2f}")
  print("="*40)
    
  return total_value, stock_value, crypto_value
if __name__ == "__main__":
  database.init_db()
  print("Fetching live data from Alpaca & Coinbase...")
  try:
    portfolio_data = get_total_portfolio()
        
    total_equity, stock_total, crypto_total = display_portfolio(portfolio_data)
        
    print("\n--- GOAL TRACKER ---")
    user_goal = input("Enter the name of your financial goal (e.g., tuition, laptop, vacation): ")
    amount_input = input(f"Enter the dollar amount needed for {user_goal}: $")
        
    try:
      target_amount = float(amount_input.replace(',', ''))
    except ValueError:
      target_amount = 0.0
            
    if target_amount > 0:
      percentage = calculate_goal_progress(total_equity, target_amount)
      remaining = max(0.0, target_amount - total_equity)
            
      print("\n" + "-"*40)
      print(f"GOAL: {user_goal.upper()}")
      print(f"TARGET:    ${target_amount:,.2f}")
      print(f"PROGRESS:  {percentage:.2f}%")
      print(f"REMAINING: ${remaining:,.2f}")
      print("-"*40 + "\n")
    else:
      print("\nInvalid amount entered. Please run again and enter a valid number.")
    database.save_snapshot(grand_total, stock_total, crypto_total)
  except Exception as e:
    print(f"\nAn error occurred while fetching data: {e}")

