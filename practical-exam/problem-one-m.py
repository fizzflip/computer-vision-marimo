import marimo

__generated_with = "0.23.1"
app = marimo.App(
    width="medium",
    layout_file="layouts/problem-one-m.grid.json",
    auto_download=["ipynb", "html"],
)


@app.cell
def _():
    import marimo as mo
    import cv2

    return cv2, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Original Image
    """)
    return


@app.cell
def _(cv2, mo):
    ## _img = cv2.imread('./sample-image.jpg')
    img = cv2.cvtColor(cv2.imread('./sample-image.jpg'), cv2.COLOR_RGB2BGR)
    mo.image(img)
    return (img,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grayscale Image
    """)
    return


@app.cell
def _(cv2, img, mo):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mo.image(img_gray)
    return (img_gray,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Resized Image (500 x 500)
    """)
    return


@app.cell
def _(cv2, img, mo):
    img_resized = cv2.resize(img, (900, 900))
    mo.image(img_resized)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cropped Image
    """)
    return


@app.cell
def _(img, mo):
    img_crop = img[500:1000, 1000: 2000]
    mo.image(img_crop)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Brightness Enhanced ( $\beta$ = 100)
    """)
    return


@app.cell
def _(cv2, img, mo):
    img_bright = cv2.convertScaleAbs(img, alpha=1, beta=100)
    mo.image(img_bright)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Contrast Enhanced ( $\alpha$ = 1.8)
    """)
    return


@app.cell
def _(cv2, img, mo):
    img_cont = cv2.convertScaleAbs(img, alpha=1.8, beta=0)
    mo.image(img_cont)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Eroded Image (iter = 5)
    """)
    return


@app.cell
def _(cv2, img_gray, mo):
    img_erode = cv2.erode(img_gray, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=5)
    mo.image(img_erode)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Gaussian Blur (kernel = 9x9, $\sigma$ = 6)
    """)
    return


@app.cell
def _(cv2, img, mo):
    gauss_blur = cv2.GaussianBlur(img, (9, 9), 6)
    mo.image(gauss_blur)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bilateral Filter ($\sigma_{color}$ = $\sigma_{space} = 72$)
    """)
    return


@app.cell
def _(cv2, img, mo):
    bilateral_blur = cv2.bilateralFilter(img, 9, 72, 72)
    mo.image(bilateral_blur)
    return


@app.cell
def _(cv2, img_gray):
    cv2.imwrite('./gray_image.jpg', img_gray)
    return


if __name__ == "__main__":
    app.run()
