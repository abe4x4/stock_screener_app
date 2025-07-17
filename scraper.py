# scraper.py

import yfinance as yf

# Function to fetch stock data for a given ticker symbol
def fetch_stock_data(ticker):
    """
    Fetch the stock data for a specific ticker symbol using yfinance.
    This will fetch historical data for one day by default.

    Arguments:
    ticker (str): The stock ticker symbol (e.g., 'AAPL', 'GOOGL')

    Returns:
    pandas.DataFrame: Stock data for the given ticker symbol
    """
    stock = yf.Ticker(ticker)  # Fetch the ticker object for the stock
    stock_data = stock.history(period="1d")  # Get daily historical data
    return stock_data  # Return the stock data
