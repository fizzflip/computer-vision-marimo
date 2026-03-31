import yfinance as yf

# Just append .NS to the ticker for NSE stocks
tcs = yf.Ticker("TCS.NS")
historical_data = tcs.history(start="2026-02-18", end="2026-02-26")

print(historical_data[['High', 'Low']])