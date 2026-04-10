import marimo

__generated_with = "0.23.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import cv2

    return cv2, mo


@app.cell
def _(mo):
    # This allows the user to upload or take a photo
    f = mo.ui.file(filetypes=[".png", ".jpg"])
    f

    return (f,)


@app.cell
def _(f):
    image = f.value[0].contents
    return


@app.cell
def _(cv2, f):
    cv2.imread(f.value[0].contents)
    return


@app.cell
def _():
    from wigglystuff import WebcamCapture

    # Create the webcam component
    camera = WebcamCapture()
    camera
    return (camera,)


@app.cell
def _(camera, mo):

    mo.image(camera.image_base64)

    return


if __name__ == "__main__":
    app.run()
