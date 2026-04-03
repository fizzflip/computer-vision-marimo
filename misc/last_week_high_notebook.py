import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium", app_title="Last Week Price High")


@app.cell
def _():
    import marimo as mo
    import yfinance as yf
    from datetime import date, timedelta

    return date, mo, timedelta, yf


@app.cell
def _(mo):
    mo.md("""
    # 📈 Last Week Price High
    Fetch the highest price recorded **last week (Mon–Fri)** for any Yahoo Finance instrument.

    **Supported formats:**
    - Stocks: `AAPL`, `TSLA`, `MSFT`
    - NSE (India): `RELIANCE.NS`, `TCS.NS`
    - BSE (India): `RELIANCE.BO`, `INFY.BO`
    - Multiple tickers: separate with commas → `AAPL, MSFT, GOOGL`
    """)
    return


@app.cell
def _(mo):
    ticker_input = mo.ui.text(
        placeholder="e.g. AAPL, RELIANCE.NS, TCS.BO",
        label="**Ticker(s)**",
        full_width=True,
    )
    ticker_input
    return (ticker_input,)


@app.cell
def _(mo):
    run_btn = mo.ui.run_button(label="Fetch Last Week High")
    run_btn
    return (run_btn,)


@app.cell
def _(date, mo, run_btn, ticker_input, timedelta, yf):
    mo.stop(not run_btn.value, mo.md("_Enter ticker(s) above and click **Fetch Last Week High**._"))

    # ── date helpers ──────────────────────────────────────────────────────────
    def last_week_range():
        today = date.today()
        this_monday = today - timedelta(days=today.weekday())
        last_monday = this_monday - timedelta(weeks=1)
        last_friday = last_monday + timedelta(days=4)
        return last_monday, last_friday

    week_start, week_end = last_week_range()

    # ── parse tickers ─────────────────────────────────────────────────────────
    raw_input = ticker_input.value.strip()
    tickers = [t.strip().upper() for t in raw_input.split(",") if t.strip()]

    mo.stop(
        not tickers,
        mo.callout(mo.md("⚠️ Please enter at least one ticker symbol."), kind="warn"),
    )

    # ── fetch data ────────────────────────────────────────────────────────────
    download_end = week_end + timedelta(days=1)
    results = []
    errors = []

    for ticker in tickers:
        try:
            raw = yf.download(
                ticker,
                start=week_start.isoformat(),
                end=download_end.isoformat(),
                progress=False,
                auto_adjust=True,
            )
            if raw.empty:
                errors.append((ticker, "No data returned — check the symbol or try again."))
                continue

            high_series = raw["High"].squeeze()
            week_high = float(high_series.max())
            high_date = high_series.idxmax().date()
            week_open = float(raw["Open"].iloc[0].squeeze())
            week_close = float(raw["Close"].iloc[-1].squeeze())
            pct_from_open = ((week_high - week_open) / week_open) * 100

            try:
                currency = yf.Ticker(ticker).fast_info.currency or "N/A"
            except Exception:
                currency = "N/A"

            results.append({
                "Ticker":       ticker,
                "Week High":    f"{week_high:,.4f}",
                "Currency":     currency,
                "Date of High": str(high_date),
                "Week Open":    f"{week_open:,.4f}",
                "Week Close":   f"{week_close:,.4f}",
                "High vs Open": f"+{pct_from_open:.2f}%" if pct_from_open >= 0 else f"{pct_from_open:.2f}%",
                "Trading Days": len(raw),
            })
        except Exception as exc:
            errors.append((ticker, str(exc)))

    # ── render ────────────────────────────────────────────────────────────────
    header = mo.md(f"### Results — week of {week_start} to {week_end}")

    if results:
        table = mo.ui.table(results, selection=None)
        results_block = mo.vstack([header, table])
    else:
        results_block = mo.vstack([header, mo.md("_No results to display._")])

    if errors:
        error_lines = "\n".join(f"- **{t}**: {msg}" for t, msg in errors)
        error_block = mo.callout(
            mo.md(f"⚠️ **Could not fetch data for:**\n\n{error_lines}"),
            kind="warn",
        )
        mo.vstack([results_block, error_block])
    else:
        results_block
    return


if __name__ == "__main__":
    app.run()
