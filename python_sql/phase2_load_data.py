import pandas as pd

file_path = (r"C:\Users\maria\Desktop\Customer_Order_Analysis_Project\data\sales_dataset_project2.xlsx")
df = pd.read_excel(file_path)

print("File loaded successfully")
print("Shape:", df.shape)
print("Columns:")
print(df.columns)
print("\nFirst 5 rows:")
print(df.head())

print(df.shape)
print(df.columns)
print(df.head())
print(df.info())

print("\n--- BASIC DATA INFO ---")
print("Shape (rows, columns):", df.shape)

print("\n--- COLUMN NAMES ---")
print(df.columns)

print("\n--- FIRST 5 ROWS ---")
print(df.head())

print("\n--- DATA TYPES & NULLS ---")
print(df.info())

# -----------------------------
# CLEAN COLUMN NAMES (SQL SAFE)
# -----------------------------
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

print("\n--- CLEANED COLUMN NAMES ---")
print(df.columns)

# Convert OrderDate to datetime
df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")

# Save cleaned data
df.to_csv(
    r"C:\Users\maria\Desktop\Customer_Order_Analysis_Project\data\cleaned_customer_orders.csv",
    index=False
)

print("Phase 2 completed: cleaned data saved")