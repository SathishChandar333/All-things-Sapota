import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("./sales_data_2.csv")

# Task 4: Calculate percentiles for buying and selling prices
buying_price_percentiles = data['Buying price'].quantile([0.25, 0.5, 0.75])
selling_price_percentiles = data['Selling price'].quantile([0.25, 0.5, 0.75])

# Print percentiles for buying and selling prices
print("\nBuying Price Percentiles")
print(buying_price_percentiles)
print("\nSelling Price Percentiles")
print(selling_price_percentiles)

# Task 5: Analyze Sapota's prices falling below 25th percentile or above 75th percentile
sapota_below_25th = data[data['Selling price'] < selling_price_percentiles[0.25]]
sapota_above_75th = data[data['Selling price'] > selling_price_percentiles[0.75]]

# Print results for Sapota's prices falling below 25th percentile or above 75th percentile
print("\nSapota's Prices Below 25th Percentile \n")
print(sapota_below_25th[['Date', 'Selling price']])
print("\nSapota's Prices Above 75th Percentile \n")
print(sapota_above_75th[['Date', 'Selling price']])