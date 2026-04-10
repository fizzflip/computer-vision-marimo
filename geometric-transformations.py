import marimo

__generated_with = "0.23.0"
app = marimo.App(
    width="medium",
    layout_file="layouts/geometric-transformations.grid.json",
    auto_download=["ipynb", "html"],
)


@app.cell
def _():
    from matplotlib import pyplot as plt
    import marimo as mo
    import numpy as np
    import cv2

    return cv2, mo, np, plt


@app.cell
def _(cv2):
    img = cv2.imread('./samples/images/nasa-sphere.jpg')
    rows, cols, ch = img.shape
    return cols, img, rows


@app.cell
def _(mo):
    A = mo.ui.slider(0, 255)
    B = mo.ui.slider(0, 255)
    A, B
    return A, B


@app.cell
def _(mo):
    C = mo.ui.slider(0, 255)
    D = mo.ui.slider(0, 255)
    C, D
    return C, D


@app.cell
def _(mo):
    E = mo.ui.slider(0, 255)
    F = mo.ui.slider(0, 255)
    E, F
    return E, F


@app.cell
def _(A, B, C, D, E, F, np):
    pts1 = np.float32([[50, 50],
                       [200, 50], 
                       [50, 200]])
    pts2 = np.float32([[A.value, B.value],
                       [C.value, D.value], 
                       [E.value, F.value]])
    return pts1, pts2


app._unparsable_cell(
    r"""
    img =
    """,
    name="_"
)


@app.cell
def _(img, mo):
    mo.image(img)
    return


@app.cell
def _():
    return


@app.cell
def _(cols, cv2, img, pts1, pts2, rows):
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return (dst,)


@app.cell
def _(img, plt):
    plt.subplot(121)
    plt.imshow(img)
    plt.title('Input')
    return


@app.cell
def _(dst, plt):
    plt.subplot(122)
    plt.imshow(dst)
    plt.title('Output')
    return


@app.cell
def _(dst, mo):
    mo.image(dst)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
