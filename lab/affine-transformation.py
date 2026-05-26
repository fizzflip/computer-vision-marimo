import marimo

__generated_with = "0.22.0"
app = marimo.App()


@app.cell
def _():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    return cv2, np, plt


@app.cell
def _(cv2):
    # 1. Load the image
    img = cv2.imread('./samples/images/boat-town.jpg')
    # Convert BGR to RGB for matplotlib display
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rows, cols, ch = img_rgb.shape
    return cols, img_rgb, rows


@app.cell
def _(np):
    # 2. Define three points from the original image
    # Format: [x, y]
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    return (pts1,)


@app.cell
def _(np):
    # 3. Define where those three points should map to in the output image
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    return (pts2,)


@app.cell
def _(cv2, pts1, pts2):
    # 4. Calculate the 2x3 Affine Transformation Matrix
    M_affine = cv2.getAffineTransform(pts1, pts2)
    return (M_affine,)


@app.cell
def _(M_affine, cols, cv2, img_rgb, rows):
    # 5. Apply the transformation
    # The third argument is the size of the output image (width, height)
    dst_affine = cv2.warpAffine(img_rgb, M_affine, (cols, rows))
    return (dst_affine,)


@app.cell
def _(dst_affine, img_rgb, plt):
    # Display the results
    plt.subplot(121), plt.imshow(img_rgb), plt.title('Input')
    plt.subplot(122), plt.imshow(dst_affine), plt.title('Affine Transform')
    plt.show()
    return


if __name__ == "__main__":
    app.run()
