# main.py

from scraper import fetch_stock_data

# Test the fetch_stock_data function
data = fetch_stock_data('AAPL')  # Fetch data for Apple (AAPL)
print(data)  # Print the fetched data
