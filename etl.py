import pandas as pd

# -------- EXTRACT --------
df = pd.read_csv("sales_data.csv")

# -------- TRANSFORM --------
df = df[df['Product'].isin(['Laptop', 'Mobile'])]
df['TotalAmount'] = df['Quantity'] * df['Price']

df = df.rename(columns={
    'OrderID': 'Order ID',
    'Customer': 'Customer Name',
    'Product': 'Product Name',
    'City': 'City'
})

# -------- TABLE DISPLAY (MANUAL) --------

print("| Order ID | Customer Name | Product Name | Quantity | Price  | City   | TotalAmount |")



for _, row in df.iterrows():
    print(f"| {row['Order ID']:^8} | {row['Customer Name']:^13} | {row['Product Name']:^12} |"
          f" {row['Quantity']:^8} | {row['Price']:^6} | {row['City']:^6} | {row['TotalAmount']:^11} |")

# -------- LOAD --------
df.to_csv("sales_cleaned.csv", index=False)

