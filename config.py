# config.py

# Adjustable screening criteria for the stock screener
MIN_PRICE_INCREASE_PERCENT = 0.10  # Minimum daily price increase (10%)
MIN_VOLUME_MULTIPLIER = 5  # Minimum 5x volume surge from the average volume
MIN_STOCK_PRICE = 5  # Minimum stock price (e.g., penny stocks or higher)
MAX_STOCK_PRICE = 500  # Maximum stock price (can be adjusted)
MAX_FLOAT_MILLIONS = 100  # Maximum float in millions (less float = more volatility)
NEWS_SEARCH_DAYS_BACK = 7  # How many days back to consider relevant news
NEWS_KEYWORDS = ['breakout', 'positive', 'announcement', 'acquisition']  # Keywords for news screening
MAX_WORKERS = 10  # Number of threads to speed up data fetching

