import marimo

__generated_with = "0.20.2"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import cv2

    return cv2, mo


@app.cell
def _():
    img_path = './samples/images/visual-qr-codes.jpg'
    return (img_path,)


@app.cell
def _(img_path, mo):
    mo.image(img_path)
    return


@app.cell
def _(cv2, img_path):
    img = cv2.imread(img_path, 0)
    return (img,)


@app.cell
def _(img, mo):
    mo.image(img)
    return


@app.cell
def _(cv2, img):
    qcd = cv2.QRCodeDetector()

    retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
    return decoded_info, points, retval, straight_qrcode


@app.cell
def _(retval):
    retval
    return


@app.cell
def _(decoded_info):
    decoded_info
    return


@app.cell
def _(points):
    points
    return


@app.cell
def _(straight_qrcode):
    straight_qrcode
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
