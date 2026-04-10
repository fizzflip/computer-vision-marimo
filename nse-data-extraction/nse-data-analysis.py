import marimo

__generated_with = "0.23.0"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import requests
    import pandas as pd

    return pd, requests


@app.cell
def _(mo):
    index = mo.ui.dropdown(
        options=[
            "NIFTY 50",
            "NIFTY BANK",
            "NIFTY IT",
            "NIFTY FMCG",
            "NIFTY AUTO",
        ],
        value="NIFTY 50",
        label="Select NSE Index",
    )
    index
    return (index,)


@app.cell
def _(index, requests):
    def fetch_nse_index(index_name):
        url = "https://www.nseindia.com/api/equity-stockIndices"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            ),
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.nseindia.com/market-data/live-equity-market",
        }

        session = requests.Session()
        session.headers.update(headers)

        # First request to get cookies
        session.get("https://www.nseindia.com")

        # Actual API call
        response = session.get(url, params={"index": index_name})
        response.raise_for_status()

        return response.json()


    raw_data = fetch_nse_index(index.value)
    raw_data
    return (raw_data,)


@app.cell
def _(pd, raw_data):
    def normalize_index_data(raw_json):
        df = pd.json_normalize(raw_json["data"])

        # Rename columns to snake_case & readable names
        rename_map = {
            "symbol": "symbol",
            "open": "open",
            "dayHigh": "high",
            "dayLow": "low",
            "lastPrice": "last_price",
            "previousClose": "prev_close",
            "change": "change",
            "pChange": "percent_change",
            "totalTradedVolume": "volume",
            "totalTradedValue": "traded_value",
            "yearHigh": "year_high",
            "yearLow": "year_low",
            "nearWKH": "pct_from_52w_high",
            "nearWKL": "pct_from_52w_low",
        }

        df = df.rename(columns=rename_map)

        # Convert numeric columns safely
        numeric_cols = [
            "open", "high", "low", "last_price", "prev_close",
            "change", "percent_change", "volume", "traded_value",
            "year_high", "year_low", "pct_from_52w_high", "pct_from_52w_low"
        ]

        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        # Add timestamp
        df["timestamp"] = pd.Timestamp.now('Asia/Kolkata')

        # Optional: reorder columns
        preferred_order = [
            "symbol", "last_price", "change", "percent_change",
            "open", "high", "low", "prev_close",
            "volume", "traded_value",
            "year_high", "year_low",
            "pct_from_52w_high", "pct_from_52w_low",
            "timestamp"
        ]

        df = df[[c for c in preferred_order if c in df.columns]]

        return df

    df = normalize_index_data(raw_data)
    df
    return (df,)


@app.cell
def _(df):
    df.describe()
    return


if __name__ == "__main__":
    app.run()
