import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import cv2
    return cv2, mo


@app.cell
def _(cv2):
    img_gray = cv2.imread('./images/wallhaven-d8gygl.png')
    return (img_gray,)


@app.cell
def _(img_gray, mo):
    mo.image(img_gray)
    return


@app.cell
def _(cv2, img_gray):
    img_gauss = cv2.GaussianBlur(img_gray, (11, 11), 900)
    return (img_gauss,)


@app.cell
def _(img_gauss, mo):
    mo.image(img_gauss)
    return


@app.cell
def _(cv2, img_gray):
    img_median = cv2.medianBlur(img_gray, 11)
    return (img_median,)


@app.cell
def _(img_median, mo):
    mo.image(img_median)
    return


@app.cell
def _(cv2, img_gray):
    img_bilat = cv2.bilateralFilter(img_gray, 299, 299, 299)
    return (img_bilat,)


@app.cell
def _(img_bilat, mo):
    mo.image(img_bilat)
    return


if __name__ == "__main__":
    app.run()
