import sqlite3
from datetime import datetime


DB_NAME = "portfolio.db"

def init_db():
  """creates db and table if they do not exist"""
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()

  cursor.execute('''
      CREATE TABLE IF NOT EXISTS portfolio_history (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        total_equity REAL,
        stock_equity real,
        crypto_equity REAL

  
      )
  ''')
  conn.commit()
  conn.close()
def save_snapshot(total_equity, stock_equity, crypto_equity):
  """Saves current port w timestamp"""
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()

  #get current data and timestamp
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  cursor.execute('''
    INSERT INTO portfolio_history (timestamp, total_equity, stock_equity, crypto_equity)
    VALUES(?, ?, ?, ?)
  ''',  (timestamp, total_equity, stock_equity, crypto_equity))
  conn.commit()
  conn.close()

  print(f"[*] Snapshot saved to database at {timestamp}")
if __name__ == "__main__":
  init_db()
  print("Database initialized succesfully")

  