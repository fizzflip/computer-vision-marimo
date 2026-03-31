import marimo

__generated_with = "0.19.8"
app = marimo.App(width="medium", auto_download=["ipynb", "html"])


@app.cell
def _():
    import marimo as mo
    import cv2
    import numpy as np

    return cv2, mo, np


@app.cell
def _(np):
    def median_filter(image, ksize=3, stride=1):
        """
        image  : grayscale image (H x W)
        ksize  : kernel size (odd number)
        stride : how far the kernel moves each step
                 stride=1   -> overlapping
                 stride=ksize -> non-overlapping
        """

        pad = ksize // 2
        padded = np.pad(image, pad, mode="edge")

        H, W = image.shape

        # Output size depends on stride
        out_h = (H - 1) // stride + 1
        out_w = (W - 1) // stride + 1
        output = np.zeros((out_h, out_w), dtype=np.uint8)

        out_y = 0
        for y in range(0, H, stride):
            out_x = 0
            for x in range(0, W, stride):
                # Extract kernel window
                window = padded[y : y + ksize, x : x + ksize]

                # Median value
                output[out_y, out_x] = np.median(window)

                out_x += 1
            out_y += 1

        return output

    return (median_filter,)


@app.cell
def _(cv2, median_filter):

    # Load image as grayscale
    img = cv2.imread("./samples/images/nasa-sphere.jpg", cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise ValueError("Image not found.")

    ksize = 5

    # 1) Overlapping kernel (standard median blur)
    overlap_result = median_filter(img, ksize=ksize, stride=1)

        # 2) Non-overlapping kernel
    non_overlap_result = median_filter(img, ksize=ksize, stride=ksize)

        # Save results
    cv2.imwrite("median_overlap.jpg", overlap_result)
    cv2.imwrite("median_non_overlap.jpg", non_overlap_result)

    print("Done. Saved overlapping and non-overlapping median blur images.")
    return non_overlap_result, overlap_result


@app.cell
def _(mo, overlap_result):
    mo.image(overlap_result)
    return


@app.cell
def _(mo, non_overlap_result):
    mo.image(non_overlap_result)
    return


if __name__ == "__main__":
    app.run()
