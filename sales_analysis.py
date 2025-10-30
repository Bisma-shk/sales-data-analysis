# Retail Sales Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Create Sample Sales Data ---
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Electronics': [12000, 15000, 17000, 14000, 18000, 22000, 25000, 23000, 21000, 26000, 30000, 35000],
    'Clothing': [8000, 9500, 10000, 9000, 11000, 13000, 14000, 13500, 12000, 12500, 16000, 19000],
    'Home_Appliances': [7000, 8500, 9000, 9500, 10500, 11500, 12500, 13000, 12000, 15000, 17000, 20000]
}

df = pd.DataFrame(data)

# --- Step 2: Compute Total Sales per Month ---
df['Total_Sales'] = df['Electronics'] + df['Clothing'] + df['Home_Appliances']

# --- Step 3: Display Summary ---
print("📊 Sales Data Overview:\n")
print(df.describe())

# --- Step 4: Plot Monthly Sales Trend ---
plt.figure(figsize=(10,5))
plt.plot(df['Month'], df['Total_Sales'], marker='o', linewidth=2)
plt.title('Monthly Total Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales (in ₹)')
plt.grid(True)
plt.show()

# --- Step 5: Plot Category-wise Sales ---
df.plot(x='Month', y=['Electronics', 'Clothing', 'Home_Appliances'], kind='bar', figsize=(10,5))
plt.title('Category-wise Monthly Sales')
plt.ylabel('Sales (in ₹)')
plt.show()

# --- Step 6: Top Category by Total Sales ---
category_totals = df[['Electronics', 'Clothing', 'Home_Appliances']].sum()
top_category = category_totals.idxmax()
print(f"\n🏆 Top-performing Category: {top_category} with total sales of ₹{category_totals[top_category]:,}")
