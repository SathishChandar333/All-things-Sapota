import pandas as pd

# Load the data
data = pd.read_csv("./sales_data_1.csv")

# Calculate profit for each transaction
data['Profit'] = data['Selling price'] - data['Buying price']

# Calculate overall gross margin
total_buying_price = data['Buying price'].sum()
total_selling_price = data['Selling price'].sum()
overall_gross_margin = ((total_selling_price - total_buying_price) / total_buying_price) * 100

# Calculate profit for each vendor
vendor_profit = data.groupby('Firm bought from')['Profit'].sum()
most_profitable_vendor = vendor_profit.idxmax()

# Calculate profit for each customer
customer_profit = data.groupby('Customer')['Profit'].sum()
least_profitable_customer = customer_profit.idxmin()

# Calculate profit for each day
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%y')
data['Day'] = data['Date'].dt.day_name()
day_profit = data.groupby('Day')['Profit'].sum()
most_profitable_day = day_profit.idxmax()
least_profitable_day = day_profit.idxmin()

print('overall_gross_margin: ', overall_gross_margin)
print('most_profitable_vendor: ', most_profitable_vendor)
print('least_profitable_customer: ', least_profitable_customer)
print('most_profitable_day: ', most_profitable_day)
print('least_profitable_day: ', least_profitable_day)
