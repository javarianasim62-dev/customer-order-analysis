import sqlite3
import pandas as pd
import os

# Project paths
project_root = r"C:\Users\maria\Desktop\Customer_Order_Analysis_Project"
data_path = os.path.join(project_root, "data")
db_path = os.path.join(data_path, "customer_orders.db")
csv_path = os.path.join(data_path, "cleaned_customer_orders.csv")

# Load cleaned CSV
df = pd.read_csv(csv_path)

# Connect to SQLite
conn = sqlite3.connect(db_path)

# Create SQL table
df.to_sql("orders", conn, if_exists="replace", index=False)

# Verify table creation
tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("Phase 3 completed: Database created successfully")
print("Tables in database:")
print(tables)

conn.close()