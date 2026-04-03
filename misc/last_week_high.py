#!/usr/bin/env python3
"""
last_week_high.py
-----------------
Fetches the price high for the previous calendar week (Mon–Fri)
for any Yahoo Finance instrument: stocks, ETFs, forex, crypto, indices, etc.

Usage:
    python last_week_high.py <TICKER> [<TICKER2> ...]

Examples:
    python last_week_high.py AAPL
    python last_week_high.py AAPL MSFT TSLA
    python last_week_high.py BTC-USD
    python last_week_high.py EURUSD=X
    python last_week_high.py SPY QQQ GLD
    python last_week_high.py ^GSPC          # S&P 500 index

Requirements:
    pip install yfinance
"""

import sys
from datetime import date, timedelta
import yfinance as yf


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------

def last_week_range() -> tuple[date, date]:
    """
    Return (monday, friday) of the most recently completed Mon–Fri week.
    'Last week' is defined as the ISO week that ended before today's week.
    """
    today = date.today()
    # ISO weekday: Monday=1 … Sunday=7
    # Start of *this* week (Monday)
    this_monday = today - timedelta(days=today.weekday())
    # Last week's Monday and Friday
    last_monday = this_monday - timedelta(weeks=1)
    last_friday = last_monday + timedelta(days=4)
    return last_monday, last_friday


# ---------------------------------------------------------------------------
# Core logic
# ---------------------------------------------------------------------------

def fetch_last_week_high(ticker: str) -> dict:
    """
    Download OHLCV data for the previous week and return a result dict with:
        ticker, week_start, week_end, high, high_date, currency
    Raises ValueError if no data is found.
    """
    week_start, week_end = last_week_range()

    # yfinance's end date is *exclusive*, so add one day
    download_end = week_end + timedelta(days=1)

    raw = yf.download(
        ticker,
        start=week_start.isoformat(),
        end=download_end.isoformat(),
        progress=False,
        auto_adjust=True,
    )

    if raw.empty:
        raise ValueError(
            f"No data returned for '{ticker}'. "
            "Check the ticker symbol and ensure the market was open last week."
        )

    # When downloading a single ticker, columns are simple strings.
    # Grab the High column and find the max.
    high_series = raw["High"]
    if hasattr(high_series, "squeeze"):          # multi-level columns fallback
        high_series = high_series.squeeze()

    week_high = float(high_series.max())
    high_date = high_series.idxmax()

    # Try to retrieve the currency (works for most assets)
    try:
        info = yf.Ticker(ticker).fast_info
        currency = getattr(info, "currency", "N/A")
    except Exception:
        currency = "N/A"

    return {
        "ticker":     ticker.upper(),
        "week_start": week_start,
        "week_end":   week_end,
        "high":       week_high,
        "high_date":  high_date.date() if hasattr(high_date, "date") else high_date,
        "currency":   currency,
        "days_seen":  len(raw),
    }


# ---------------------------------------------------------------------------
# Display
# ---------------------------------------------------------------------------

def print_result(result: dict) -> None:
    currency = result["currency"]
    symbol   = "" if currency in ("N/A", None) else f" {currency}"
    print(
        f"  {result['ticker']:<12} "
        f"Week: {result['week_start']} → {result['week_end']}  |  "
        f"High: {result['high']:>12,.4f}{symbol}  "
        f"(on {result['high_date']}, {result['days_seen']} trading day(s))"
    )


def print_error(ticker: str, err: Exception) -> None:
    print(f"  {ticker.upper():<12} ERROR — {err}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    tickers = sys.argv[1:]
    week_start, week_end = last_week_range()

    print(f"\n{'='*70}")
    print(f"  Last-Week Price High   ({week_start}  to  {week_end})")
    print(f"{'='*70}")

    for ticker in tickers:
        try:
            result = fetch_last_week_high(ticker)
            print_result(result)
        except Exception as exc:
            print_error(ticker, exc)

    print(f"{'='*70}\n")


if __name__ == "__main__":
    main()
