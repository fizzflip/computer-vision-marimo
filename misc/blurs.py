import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import cv2

    return cv2, mo


@app.cell
def _(cv2, mo):
    img = cv2.imread("./samples/images/head-cross-section.webp")
    mo.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    return (img,)


@app.cell
def _():
    return


@app.cell
def _(cv2, img, mo):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mo.image(img_gray)
    return (img_gray,)


@app.cell
def _(mo):
    kernel_size = mo.ui.slider(1, 100, 2)
    kernel_size
    return (kernel_size,)


@app.cell
def _(cv2, img_gray, kernel_size, mo):
    img_gaus_blur = cv2.GaussianBlur(img_gray, (kernel_size.value, kernel_size.value), kernel_size.value)
    mo.image(img_gaus_blur)
    # print(cv2.BORDER_DEFAULT)
    return (img_gaus_blur,)


@app.cell
def _(cv2, img_gray, kernel_size, mo):
    img_med_blur = cv2.medianBlur(img_gray, kernel_size.value)
    mo.image(img_med_blur)
    return


@app.cell
def _(cv2, img_gaus_blur, mo):
    img_sobel = cv2.Sobel(img_gaus_blur, cv2.CV_64F, 0, 1, ksize=5)
    mo.image(img_sobel)
    return


@app.cell
def _(cv2, img_gaus_blur, mo):
    img_sobel_sd = cv2.Sobel(img_gaus_blur, int(-1/cv2.CV_64F), 1, 0, ksize=5)
    mo.image(img_sobel_sd)
    return


@app.cell
def _(mo):
    th_low = mo.ui.slider(0, 255)
    th_high = mo.ui.slider(0, 255)
    (th_low, th_high)
    return th_high, th_low


@app.cell
def _(cv2, img_gaus_blur, mo, th_high, th_low):
    img_canny = cv2.Canny(img_gaus_blur, th_low.value, th_high.value)
    mo.image(img_canny)
    return


if __name__ == "__main__":
    app.run()
