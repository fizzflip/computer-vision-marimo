import marimo

__generated_with = "0.19.6"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import cv2
    return (cv2,)


@app.cell
def _(cv2):
    vid = cv2.VideoCapture('/home/mrbot/Documents/devenvs/marimo/Class/Test Jellyfin 1080p AVC 3M.mp4')
    return (vid,)


@app.cell
def _(vid):
    vid.grab()
    return


if __name__ == "__main__":
    app.run()
