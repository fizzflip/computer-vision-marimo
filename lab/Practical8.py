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
    img = cv2.imread('./images/i.webp')
    return (img,)


@app.cell
def _(img, mo):
    mo.image(img)
    return


@app.cell
def _(cv2, img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return (img_gray,)


@app.cell
def _(img_gray, mo):
    mo.image(img_gray)
    return


@app.cell
def _(cv2, img_gray):
    img_canny = cv2.Canny(img_gray, 195, 200)
    return (img_canny,)


@app.cell
def _(img_canny, mo):
    mo.image(img_canny)
    return


if __name__ == "__main__":
    app.run()
