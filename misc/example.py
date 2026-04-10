import marimo

__generated_with = "0.23.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # 🧪 Standalone Marimo Demo

    This notebook:
    - runs in the browser
    - keeps interactivity after export
    - requires **no Python backend** when exported
    """)
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(
        start=0,
        stop=100,
        value=50,
        label="Pick a number",
    )

    checkbox = mo.ui.checkbox(label="Double it?", value=False)

    mo.vstack([slider, checkbox])
    return checkbox, slider


@app.cell
def _(checkbox, mo, slider):
    value = slider.value
    result = value * 2 if checkbox.value else value

    mo.md(
        f"""
        ## Result

        **Input:** {value}  
        **Output:** `{result}`
        """
    )
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🎉 Why this matters

    After export, this runs entirely in:
    - WebAssembly
    - your browser
    - with zero servers
    """)
    return


if __name__ == "__main__":
    app.run()
