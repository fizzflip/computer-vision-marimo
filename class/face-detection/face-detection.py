import marimo

__generated_with = "0.23.0"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import cv2

    return cv2, mo


@app.cell
def _(mo):
    f = mo.ui.file(kind="area")
    f
    return (f,)


@app.cell
def _(f):
    f.value
    return


@app.cell
def _(cv2):

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    return (face_cascade,)


@app.cell
def _(cv2, mo):
    image = cv2.imread('./samples/images/crowd-low-res.jpg')
    mo.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    return (image,)


@app.cell
def _(cv2, image, mo):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    mo.image(gray_image)
    return (gray_image,)


@app.cell
def _(face_cascade, gray_image):
    faces = face_cascade.detectMultiScale(
        gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    faces
    return (faces,)


@app.cell
def _(cv2, faces, image):
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)
        cv2.rectangle(image, (x, y+h), (x+w, y+h+20), (255, 0, 0), -1)
    return


@app.cell
def _(cv2, image, mo):
    mo.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
