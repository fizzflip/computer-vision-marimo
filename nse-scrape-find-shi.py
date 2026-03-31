# Replace 'import requests' with the curl_cffi version
from curl_cffi import requests
import json


def fetch_nse_historical_data(symbol, start_date, end_date):
    # 1. The Magic Wand: Impersonate a real Chrome browser at the TLS level
    session = requests.Session(impersonate="chrome")

    # We no longer need a massive User-Agent string; curl_cffi handles the heavy lifting
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/"
    }

    session.headers.update(headers)
    base_url = "https://www.nseindia.com"

    print("1. Performing the TLS-spoofed Cookie Handshake...")
    try:
        session.get(base_url, timeout=10)
    except Exception as e:
        print(f"Handshake failed: {e}")
        return

    api_url = f"https://www.nseindia.com/api/historical/cm/equity?symbol={symbol}&series=[%22EQ%22]&from={start_date}&to={end_date}"
    print(f"2. Fetching historical data from: {api_url}")

    try:
        response = session.get(api_url, timeout=10)

        # Check if the server still threw a 503
        if response.status_code != 200:
            print(f"Server rejected the request. Status Code: {response.status_code}")
            return

        data = response.json()

        if "data" not in data or len(data["data"]) == 0:
            print("No data found. (Check if dates are weekends/holidays)")
            return

        weekly_high = 0.0
        weekly_low = float('inf')

        for day in data["data"]:
            high = day.get("CH_TRADE_HIGH_PRICE", 0.0)
            low = day.get("CH_TRADE_LOW_PRICE", float('inf'))

            if high > weekly_high: weekly_high = high
            if low < weekly_low: weekly_low = low

        print("\n=== Calculated Swing Trading Metrics ===")
        print(f"Last Week High: ₹{weekly_high}")
        print(f"Last Week Low:  ₹{weekly_low}")

    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    fetch_nse_historical_data("TCS", "18-02-2026", "25-02-2026")