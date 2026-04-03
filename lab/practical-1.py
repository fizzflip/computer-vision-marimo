import marimo

__generated_with = "0.19.8"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import cv2

    return cv2, mo


@app.cell
def _(cv2, mo):
    img = cv2.imread('./samples/images/boat-town.jpg')
    mo.image(img)
    return (img,)


@app.cell
def _(img, mo):
    img_crop = img[400:2000, 400:2000]
    mo.image(img_crop)
    return (img_crop,)


@app.cell
def _(mo):
    mo.pdf(
        src="https://arxiv.org/pdf/2104.00282.pdf",
        width="100%",
        height="50vh",
    )
    return


@app.cell
def _(cv2, img_crop):
    cv2.imwrite('./samples/images/new_image.png', img_crop)
    return


@app.cell
def _(cv2, img, mo):
    img_resized = cv2.resize(img, (500, 500))
    mo.image(img_resized)
    return


@app.cell
def _(cv2, img, mo):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mo.image(img_hsv)
    return (img_hsv,)


@app.cell
def _(cv2, img, img_hsv, mo):
    img_bit_or = cv2.bitwise_or(img, img_hsv)
    mo.image(img_bit_or)
    return


if __name__ == "__main__":
    app.run()
