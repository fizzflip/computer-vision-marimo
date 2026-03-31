import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import yfinance as yf

    return (yf,)


@app.cell
def _(yf):
    tcs = yf.Ticker("TCS.NS")
    return (tcs,)


@app.cell
def _(tcs):
    historical_data = tcs.history(start="2026-02-18", end="2026-02-26")
    historical_data
    return (historical_data,)


@app.cell
def _(historical_data):
    historical_data[['High', 'Low']]
    return


@app.cell
def _():
    from datetime import date, timedelta, datetime

    return date, datetime, timedelta


@app.cell
def _(date):
    date.today()
    return


@app.cell
def _(datetime):
    datetime.now()
    return


@app.cell
def _(date, timedelta):
    weekday = date.weekday(date.today())
    week_start = date.today() - timedelta(days=weekday + 7)
    week_end = week_start + timedelta(days=6)
    return week_end, week_start


@app.cell
def _(week_end, week_start):
    week_start, week_end
    return


@app.cell
def _(week_end, week_start, yf):

    infy = yf.Ticker("INFY.NS")
    infy_historical_data = infy.history(start=str(week_start), end=str(week_end))
    return (infy_historical_data,)


@app.cell
def _(infy_historical_data):
    last_week_high = max(infy_historical_data['High'])
    return (last_week_high,)


@app.cell
def _(last_week_high):
    last_week_high
    return


if __name__ == "__main__":
    app.run()
