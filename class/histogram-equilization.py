import marimo

__generated_with = "0.19.7"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import cv2
    return cv2, mo


@app.cell
def _(cv2, mo):
    img = cv2.imread("./samples/images/jp-boat-town.jpg", 0)
    mo.image(img)
    return (img,)


@app.cell
def _(cv2, img, mo):
    img_eq_hist = cv2.equalizeHist(img)
    mo.image(img_eq_hist)
    return


@app.cell
def _(mo):
    gridSize = mo.ui.slider(1, 100)
    gridSize
    return (gridSize,)


@app.cell
def _(cv2, gridSize, img, mo):
    img_eq_clh = cv2.createCLAHE(
        clipLimit=5, tileGridSize=(gridSize.value, gridSize.value)
    ).apply(img)
    mo.image(img_eq_clh)
    return


if __name__ == "__main__":
    app.run()
