# main.py

from scraper import fetch_stock_data
from analysis import analyze_price_momentum, analyze_volume_surge
from config import *

def screen_stock(ticker):
    """
    Screens a stock by checking if it meets the price momentum,
    volume surge, and news catalyst criteria.
    """
    stock_data = fetch_stock_data(ticker)  # Fetch stock data
    if analyze_price_momentum(stock_data) and analyze_volume_surge(stock_data):
        return ticker, stock_data['Close'][-1], "Pass"
    return None

def run_screening():
    """
    Runs the stock screening process for multiple stock tickers.
    """
    tickers = ['AAPL', 'GOOGL', 'AMZN']  # Example stock tickers
    results = []
    for ticker in tickers:
        result = screen_stock(ticker)
        if result:
            results.append(result)
    return results

if __name__ == "__main__":
    matched_stocks = run_screening()
    for stock in matched_stocks:
        print(f"Stock: {stock[0]} | Price: {stock[1]} | Status: {stock[2]}")
