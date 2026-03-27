import sqlite3
import pandas as pd
import os

# Project paths
project_root = r"C:\Users\maria\Desktop\Customer_Order_Analysis_Project"
data_path = os.path.join(project_root, "data")
db_path = os.path.join(data_path, "customer_orders.db")

# Connect to database
conn = sqlite3.connect(db_path)
print("Connected to SQL database")

# Check tables
tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)
print("Tables in database:")
print(tables)

# =========================
# SQL ANALYSIS
# =========================

# 1️⃣ Total sales by region
query_region_sales = """
SELECT region,
       SUM(sales) AS total_sales
FROM orders
GROUP BY region
ORDER BY total_sales DESC;
"""

region_sales = pd.read_sql(query_region_sales, conn)
print("\nTotal Sales by Region:")
print(region_sales)

# 2️⃣ Top 10 products by profit
query_top_products = """
SELECT product,
       SUM(profit) AS total_profit
FROM orders
GROUP BY product
ORDER BY total_profit DESC
LIMIT 10;
"""

top_products = pd.read_sql(query_top_products, conn)
print("\nTop 10 Products by Profit:")
print(top_products)

conn.close()