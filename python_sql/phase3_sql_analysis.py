import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv(
    r"C:\Users\maria\Desktop\Customer_Order_Analysis_Project\data\cleaned_customer_orders.csv"
)

# Connect to SQLite
conn = sqlite3.connect("customer_orders.db")

# Load data into SQL table
df.to_sql("orders", conn, if_exists="replace", index=False)

print("Data loaded into SQL database successfully")

query = """
SELECT 
    SUM(sales) AS total_sales
FROM orders;
"""

total_sales = pd.read_sql(query, conn)
print("\nTotal Sales:")
print(total_sales)

query = """
SELECT 
    category,
    SUM(sales) AS category_sales
FROM orders
GROUP BY category
ORDER BY category_sales DESC;
"""

category_sales = pd.read_sql(query, conn)
print("\nSales by Category:")
print(category_sales)

query = """
SELECT 
    customername,
    SUM(profit) AS total_profit
FROM orders
GROUP BY customername
ORDER BY total_profit DESC
LIMIT 5;
"""

top_customers = pd.read_sql(query, conn)
print("\nTop 5 Customers by Profit:")
print(top_customers)