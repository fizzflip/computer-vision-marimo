import marimo

__generated_with = "0.23.0"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    # Thresholding
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
    ## Load Image
    """)
    return


@app.cell
def _(cv2):
    img = cv2.imread('./samples/images/biblical-angel-attack.jpg', 0)
    return (img,)


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
def _(mo):
    mo.md(r"""
    ### Binary Thresholding
    """)
    return


@app.cell
def _(cv2, img, mo):
    mo.image(cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Inverse Binary Thresholding
    """)
    return


@app.cell
def _(cv2, img, mo):
    mo.image(cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)[1])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Thresholding to Zero
    """)
    return


@app.cell
def _(cv2, img, mo):
    mo.image(cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)[1])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Inverse Thresholding to Zero
    """)
    return


@app.cell
def _(cv2, img, mo):
    mo.image(cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)[1])
    return


if __name__ == "__main__":
    app.run()
