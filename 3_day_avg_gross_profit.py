import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("./sales_data_2.csv")

# Calculate daily gross profit
data['Daily Gross Profit'] = (data['Selling price'] - data['Buying price']) * data['Quantity sold']

# Calculate 3-day rolling average of daily gross profit
data['3-Day Avg Gross Profit'] = data['Daily Gross Profit'].rolling(window=3).mean()

# Print the 3-day average of daily gross profit
print("3-Day Average of Daily Gross Profit:")
print(data['3-Day Avg Gross Profit'].dropna())

# Plot 3-day average gross profit
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['3-Day Avg Gross Profit'], marker='o', linestyle='-', color='b')
plt.title('3-Day Average Gross Profit Trend')
plt.xlabel('Date')
plt.ylabel('3-Day Avg Gross Profit')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()