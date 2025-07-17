# analysis.py

# Price momentum analysis
def analyze_price_momentum(stock_data):
    """
    Analyzes the price momentum by comparing the current closing price with
    the first day's closing price to detect a price increase.

    Arguments:
    stock_data (pandas.DataFrame): Stock data with daily prices

    Returns:
    bool: True if price increase exceeds the threshold, False otherwise
    """
    latest_data = stock_data.iloc[-1]  # Get the last row (latest stock data)
    price_increase = (latest_data['Close'] - stock_data['Close'].iloc[0]) / stock_data['Close'].iloc[0]
    return price_increase > MIN_PRICE_INCREASE_PERCENT  # Compare to threshold

# Volume surge analysis
def analyze_volume_surge(stock_data):
    """
    Analyzes whether the stock is experiencing a surge in trading volume
    by comparing the latest volume with the average volume.

    Arguments:
    stock_data (pandas.DataFrame): Stock data with daily volumes

    Returns:
    bool: True if volume surge exceeds the threshold, False otherwise
    """
    average_volume = stock_data['Volume'].mean()  # Calculate average volume
    latest_data = stock_data.iloc[-1]  # Get the last row (latest stock data)
    volume_surge = latest_data['Volume'] / average_volume  # Compare to average
    return volume_surge > MIN_VOLUME_MULTIPLIER  # Return if surge is significant
