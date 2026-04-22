import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import cv2
    import numpy as np
    import urllib.request
    import os
    import PIL

    return cv2, mo, np, os, urllib


@app.cell
def load_cascade(os, urllib):
    cascade_path = "haarcascade_frontalface_default.xml"

    # Try primary GitHub URL, then fallback to jsDelivr CDN
    urls = [
        "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml",
        "https://cdn.jsdelivr.net/gh/opencv/opencv@master/data/haarcascades/haarcascade_frontalface_default.xml"
    ]

    success = False
    for url in urls:
        try:
            urllib.request.urlretrieve(url, cascade_path)
            # Verify the file actually downloaded and isn't empty
            if os.path.exists(cascade_path) and os.path.getsize(cascade_path) > 0:
                success = True
                break
        except Exception:
            continue

    if not success:
        raise RuntimeError("Failed to download the cascade file from all available fallback sources.")

    return (cascade_path,)


@app.cell
def ui_controls(mo):
    mo.md("### 📸 Live Face Detection Settings")

    image_upload = mo.ui.file(
        kind="area", 
        filetypes=[".jpg", ".jpeg", ".png"], 
        label="Upload an image"
    )

    # Interactive sliders for tuning detection
    scale_factor = mo.ui.slider(start=1.01, stop=1.5, step=0.01, value=1.1, label="Scale Factor (lower = more detections, slower)")
    min_neighbors = mo.ui.slider(start=1, stop=15, step=1, value=5, label="Min Neighbors (higher = fewer false positives)")
    min_size = mo.ui.slider(start=10, stop=200, step=5, value=30, label="Min Size (px)")
    show_original = mo.ui.checkbox(label="Show Original Image side-by-side", value=False)

    controls = mo.vstack([
        image_upload,
        mo.md("---"),
        mo.md("**Tune Parameters**"),
        scale_factor,
        min_neighbors,
        min_size,
        show_original,
        mo.md("---")
    ])
    return (
        controls,
        image_upload,
        min_neighbors,
        min_size,
        scale_factor,
        show_original,
    )


@app.cell
def display_controls(controls):
    # Renders the UI to the screen
    controls
    return


@app.cell
def process_image(
    cascade_path,
    cv2,
    image_upload,
    min_neighbors,
    min_size,
    mo,
    np,
    scale_factor,
    show_original,
):
    if not image_upload.value:
        output = mo.md("*Awaiting image upload...*")
    else:
        file_contents = image_upload.value[0].contents
        image_array = np.frombuffer(file_contents, np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

        # Keep a copy of the original for side-by-side comparison
        img_original = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)

        face_cascade = cv2.CascadeClassifier(cascade_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Use the live slider values
        faces = face_cascade.detectMultiScale(
            gray, 
            scaleFactor=scale_factor.value, 
            minNeighbors=min_neighbors.value, 
            minSize=(min_size.value, min_size.value)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4)

        img_processed = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        layout_items = [mo.md(f"**Detected {len(faces)} face(s)!**")]

        # Dynamically adjust layout based on the checkbox
        if show_original.value:
            layout_items.append(
                mo.hstack([
                    mo.vstack([mo.md("**Original**"), mo.image(img_original)]),
                    mo.vstack([mo.md("**Processed**"), mo.image(img_processed)])
                ], justify="center", gap=2)
            )
        else:
            layout_items.append(mo.image(img_processed, rounded=True))

        output = mo.vstack(layout_items)

    output
    return


if __name__ == "__main__":
    app.run()
