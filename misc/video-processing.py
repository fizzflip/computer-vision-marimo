import marimo

__generated_with = "0.21.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import cv2

    return cv2, mo


@app.cell
def _():
    return


@app.cell
def _(cv2):
    video = cv2.VideoCapture('./samples/videos/PXL_20260402_181749999.mp4')
    return (video,)


@app.cell
def _(mo, video):
    mo.image(video.read()[1])
    return


if __name__ == "__main__":
    app.run()
