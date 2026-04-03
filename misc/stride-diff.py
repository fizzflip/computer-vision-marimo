"""
Optimized Median Blur
---------------------
Uses NumPy vectorization instead of slow Python loops.

Requirements:
- Python 3.9+
- numpy
- opencv-python
"""

import cv2
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


# -----------------------------------------------------------
# Overlapping Median Filter (stride = 1)
# Fast vectorized implementation
# -----------------------------------------------------------
def median_filter_overlap(image: np.ndarray, ksize: int = 3) -> np.ndarray:
    pad = ksize // 2

    # Pad image
    padded = np.pad(image, pad_width=pad, mode="edge")

    # Create sliding windows view
    # Shape -> (H, W, ksize, ksize)
    windows = sliding_window_view(padded, (ksize, ksize))

    # Compute median across last two axes (kernel)
    result = np.median(windows, axis=(-1, -2))

    return result.astype(np.uint8)


# -----------------------------------------------------------
# Non-Overlapping Median Filter (stride = ksize)
# Uses reshape instead of loops
# -----------------------------------------------------------
def median_filter_non_overlap(image: np.ndarray, ksize: int = 3) -> np.ndarray:
    H, W = image.shape

    # Crop image so dimensions divide evenly by ksize
    Hc = (H // ksize) * ksize
    Wc = (W // ksize) * ksize
    cropped = image[:Hc, :Wc]

    # Reshape into blocks:
    # (H//k, k, W//k, k)
    blocks = cropped.reshape(Hc // ksize, ksize, Wc // ksize, ksize)

    # Move kernel axes together -> (H//k, W//k, k, k)
    blocks = blocks.swapaxes(1, 2)

    # Median over each block
    result = np.median(blocks, axis=(-1, -2))

    return result.astype(np.uint8)


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------
if __name__ == "__main__":

    img = cv2.imread("noisy-image.jpg", cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise ValueError("Image not found.")

    ksize = 5

    # Optimized overlapping median blur
    overlap_result = median_filter_overlap(img, ksize)

    # Optimized non-overlapping median blur
    non_overlap_result = median_filter_non_overlap(img, ksize)

    cv2.imwrite("median_overlap.jpg", overlap_result)
    cv2.imwrite("median_non_overlap.jpg", non_overlap_result)

    print("Optimized median filtering complete.")
