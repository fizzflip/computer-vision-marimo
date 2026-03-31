import marimo

__generated_with = "0.19.8"
app = marimo.App(
    width="medium",
    layout_file="layouts/convert-color-spaces.slides.json",
    auto_download=["ipynb", "html"],
)

with app.setup:
    import marimo as mo
    import cv2


@app.cell
def _():
    mo.md(r"""
    # Basic Color Space Conversion
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Reading the Image
    """)
    return


@app.cell
def _():
    img = cv2.imread("./samples/images/paris-street.jpg")
    return (img,)


@app.cell
def _():
    mo.md(r"""
    ### BGR
    Default Color Space used by OpenCV
    """)
    return


@app.cell
def _(img):
    mo.image(img)
    return


@app.cell
def _():
    mo.md(r"""
    ## Conversions
    """)
    return


@app.cell
def _():
    mo.md(r"""
    ### BGR-to-RGB
    By splitting, rearranging and merging channels
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    RGB is an **additive** color model based on how human eyes perceive light. It represents images as a combination of three primary colors.

    * **Appearance:** This is the "standard" look. It’s vibrant and represents the full spectrum of colors we see on screens.
    * **Common Use:** It is the default format for cameras and displays. However, it is often **poor for analysis** because a change in lighting (brightness) changes the values of all three channels (R, G, and B) simultaneously, making it hard to track objects under different shadows.
    """)
    return


@app.cell
def _(img):
    b, g, r = cv2.split(img)
    img_rgb = cv2.merge((r, g, b))
    mo.image(img_rgb)
    return (img_rgb,)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### BGR-to-Grayscale
    Grayscale is a single-channel color space representing intensity (black to white) without any color information.

    * **Appearance:** A classic "black and white" photo.
    * **Common Use:** This is used for **Feature Detection and Edge Detection**. Most algorithms (like Canny Edge Detection) don't need color to find the shape of an object. By dropping the color channels, you reduce the data by 66%, making the processing much faster and more efficient.
    """)
    return


@app.cell
def _(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return (img_gray,)


@app.cell
def _(img_gray):
    mo.image(img_gray)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### BGR-to-HSV

    HSV rearranges RGB data into a way that is more intuitive to humans and much more useful for machines.

    * **Hue:** The "type" of color (e.g., Red vs. Blue).
    * **Saturation:** The "intensity" or richness of the color.
    * **Value:** The "brightness" of the color.
    * **Appearance:** An HSV image looks like a "rainbow" map where colors are separated by their identity rather than their brightness.
    * **Common Use:** This is the gold standard for **Color Filtering**. If you want to track a "red ball," you simply look for a specific range of *Hue*. Even if the ball goes into a shadow, the *Hue* remains relatively constant while only the *Value* changes.
    """)
    return


@app.cell
def _(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return (img_hsv,)


@app.cell
def _(img_hsv):
    mo.image(img_hsv)
    return


@app.cell
def _():
    mo.md(r"""
    ### BGR-to-YUV

    YUV splits an image into **Luminance (Y)**—the brightness—and **Chrominance (U and V)**—the color difference.

    * **Appearance:** The Y channel looks like a grayscale image, while the U and V channels look like eerie, washed-out blue/red ghosts of the original.
    * **Common Use:** YUV is heavily used in **Video Compression and Transmission** (like MPEG or JPEG). Since the human eye is more sensitive to changes in brightness than color, we can "compress" the U and V channels more aggressively to save bandwidth without the viewer noticing a drop in quality.
    """)
    return


@app.cell
def _(img):
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    return (img_yuv,)


@app.cell
def _(img_yuv):
    mo.image(img_yuv)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Export Images
    """)
    return


@app.cell
def _(img_gray, img_hsv, img_rgb, img_yuv):
    for imgv, name in [(img_gray, 'grayscale'), (img_hsv, 'hsv'), (img_rgb, 'rgb'), (img_yuv, 'yuv')]:
        cv2.imwrite(filename=f'paris-street-{name}.jpg', img=imgv)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Summary

    | Color Space | Best Known For | Typical Application | Why? |
    | --- | --- | --- | --- |
    | **RGB** | Displaying images | Computer monitors, cameras, web design. | Standard format for camera sensors/datasets. |
    | **HSV** | Color isolation | Object tracking (e.g., finding a yellow taxi). |  Hue is stable under different lighting. |
    | **Grayscale** | Simplicity/Speed | Face detection, OCR (text reading), edge detection. |Reduces noise and speeds up math. |
    | **YUV** | Efficient storage | Video streaming, television broadcasting. | Avoids the cost of converting video frames. |
    """)
    return


if __name__ == "__main__":
    app.run()
