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

# =========================
# QUERY 1: Sales by Region
# =========================
query_region_sales = """
SELECT region,
       SUM(sales) AS total_sales
FROM orders
GROUP BY region
ORDER BY total_sales DESC;
"""

region_sales = pd.read_sql(query_region_sales, conn)

region_csv_path = os.path.join(data_path, "sales_by_region.csv")
region_sales.to_csv(region_csv_path, index=False)

print("Exported: sales_by_region.csv")

# =========================
# QUERY 2: Top 10 Products by Profit
# =========================
query_top_products = """
SELECT product,
       SUM(profit) AS total_profit
FROM orders
GROUP BY product
ORDER BY total_profit DESC
LIMIT 10;
"""

top_products = pd.read_sql(query_top_products, conn)

products_csv_path = os.path.join(data_path, "top_10_products_by_profit.csv")
top_products.to_csv(products_csv_path, index=False)

print("Exported: top_10_products_by_profit.csv")

conn.close()
print("Phase 5 completed successfully")