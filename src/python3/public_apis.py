import yfinance as yf

# Retrieve stock data for Apple (AAPL)
aapl = yf.Ticker("AAPL")

# Get historical market data for the last 5 days
hist = aapl.history(period="5d")

# Get the lowest price from the last 5 days
lowest_price = hist['Low'].min()

# Print the lowest price
print(f"For AAPL, The lowest price in the last 5 days was: ${lowest_price:.2f}")