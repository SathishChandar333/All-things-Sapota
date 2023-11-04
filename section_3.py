import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("./sales_data_2.csv")

# Calculate gross margin for each vendor
data['Gross Margin'] = data['Selling price'] - data['Buying price']

# Group data by vendor and calculate the mean gross margin for each vendor
vendor_gross_margin = data.groupby('Firm bought from')['Gross Margin'].mean()

# Find the vendor with the maximum average gross margin
strategic_vendor = vendor_gross_margin.idxmax()

# Calculate theoretical max margin for the strategic vendor
theoretical_max_margin = data[data['Firm bought from'] == strategic_vendor]['Gross Margin'].max()

print(f"Strategic Vendor: {strategic_vendor}")
print(f"Theoretical Maximum Margin: {theoretical_max_margin}")

# Calculate percentage change in quantity demanded and price
initial_quantity = data['Quantity sold'].iloc[0]
final_quantity = data['Quantity sold'].iloc[-1]
quantity_change = ((final_quantity - initial_quantity) / initial_quantity) * 100

initial_price = data['Selling price'].iloc[0]
final_price = data['Selling price'].iloc[-1]
price_change = ((final_price - initial_price) / initial_price) * 100

# Calculate price elasticity of Sapota
price_elasticity = quantity_change / price_change

print(f"Price Elasticity of Sapota: {price_elasticity}")