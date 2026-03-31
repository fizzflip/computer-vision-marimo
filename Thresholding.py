import marimo

__generated_with = "0.19.7"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    # Thresholding :rocket:
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Import
    """)
    return


@app.cell
def _():
    import cv2
    import marimo as mo
    return cv2, mo


@app.cell
def _(mo):
    mo.md(r"""
    ## Original Image
    """)
    return


@app.cell
def _():
    import imutils
    img = imutils.url_to_image('https://w.wallhaven.cc/full/qr/wallhaven-qrjmgl.jpg')
    return (img,)


@app.cell
def _():
    # img = cv2.imread('./samples/images/biblical-angel-attack.jpg')
    # mo.show(img.)
    return


@app.cell
def _(img, mo):
    mo.image(img)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## Thresholding
    """)
    return


@app.cell
def _():
    thresheld_imgs = {}
    return (thresheld_imgs,)


@app.cell
def _(mo):
    T = mo.ui.slider(0, 255)
    T
    return (T,)


@app.cell
def _(mo):
    Tmax = mo.ui.slider(0, 255)
    Tmax
    return (Tmax,)


@app.cell
def _(T, mo):
    mo.md(rf"""
    $T: {T.value}$
    """)
    return


@app.cell
def _(Tmax, mo):
    mo.md(rf"""
    $T_m: {Tmax.value}$
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Binary Thresholding
    """)
    return


@app.cell
def _(T, cv2, img, mo, thresheld_imgs):
    thresheld_imgs["binary"] = cv2.threshold(img, T.value, 120, cv2.THRESH_BINARY)[1]
    mo.image(thresheld_imgs["binary"])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Inverse Binary Thresholding
    """)
    return


@app.cell
def _(T, cv2, img, mo, thresheld_imgs):
    thresheld_imgs["inverse_binary"] = cv2.threshold(img, T.value, 255, cv2.THRESH_BINARY_INV)[1]
    mo.image(thresheld_imgs["inverse_binary"])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Thresholding to Zero
    """)
    return


@app.cell
def _(T, cv2, img, mo, thresheld_imgs):
    thresheld_imgs["zero"] = cv2.threshold(img, T.value, 255, cv2.THRESH_TOZERO)[1]
    mo.image(thresheld_imgs["zero"])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Inverse Thresholding to Zero
    """)
    return


@app.cell
def _(T, cv2, img, mo, thresheld_imgs):
    thresheld_imgs["inverse_zero"] = cv2.threshold(img, T.value, 255, cv2.THRESH_TOZERO_INV)[1]
    mo.image(thresheld_imgs["inverse_zero"])
    return


if __name__ == "__main__":
    app.run()
