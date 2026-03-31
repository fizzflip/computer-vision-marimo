import marimo

__generated_with = "0.19.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import cv2

    return cv2, mo, np


@app.cell
def _(cv2, mo):
    img = cv2.imread('./samples/images/abstract-red-triangles.jpg')
    mo.image(img)
    return (img,)


@app.cell
def _(cv2, img, mo):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mo.image(img_rgb)
    return


@app.cell
def _(cv2, img, mo):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mo.image(img_gray)
    return (img_gray,)


@app.cell
def _(np):
    kernel = np.ones((1,1), np.uint8)
    return (kernel,)


@app.cell
def _(cv2, img_gray, iterations, kernel, mo):
    mo.image(cv2.erode(img_gray, kernel, iterations.value))
    return


@app.cell
def _(mo):
    iterations = mo.ui.slider(0, 1000)
    iterations
    return (iterations,)


@app.cell
def _(cv2, img_gray, iterations, kernel, mo):
    mo.image(cv2.dilate(img_gray, kernel, iterations.value))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Global Thresholding
    """)
    return


@app.cell
def _(T, cv2, img_gray, mo):
    img_thr_bin = cv2.threshold(img_gray, T.value, 255, cv2.THRESH_BINARY)[1]
    mo.image(img_thr_bin)
    return


@app.cell
def _(mo):
    T = mo.ui.slider(0, 255)
    T
    return (T,)


@app.cell
def _(mo):
    mo.md(r"""
    ### Otsu's (Automatic Global) Thresholding
    """)
    return


@app.cell
def _(cv2, img_gray, mo):
    img_thr_bin_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    mo.image(img_thr_bin_otsu)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ###
    """)
    return


@app.cell
def _(cv2, img_gray, mo):
    img_thr_adp_gauss = cv2.adaptiveThreshold(
        img_gray, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        5, 5
    )
    mo.image(img_thr_adp_gauss)
    return


@app.cell
def _(cv2, img, mo):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mo.image(img_hsv)
    return (img_hsv,)


@app.cell
def _(np):
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([0, 255, 255])
    return lower_red, upper_red


@app.cell
def _(cv2, img, img_hsv, lower_red, mo, upper_red):
    mask_color_thr = cv2.inRange(img_hsv, lower_red, upper_red)
    result = cv2.bitwise_and(img, img, mask=mask_color_thr)
    mo.image(result)
    return


if __name__ == "__main__":
    app.run()
