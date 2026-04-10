import marimo

__generated_with = "0.23.0"
app = marimo.App(width="medium")


@app.cell
def __imports():
    import marimo as mo
    import cv2
    import numpy as np

    return cv2, mo, np


@app.cell
def __header(mo):
    mo.md("""
    # 🕵️‍♂️ Interactive Face Detection
    Upload an image using the file browser below. Adjust the **Scale Factor** and **Min Neighbors** sliders to see how the Haar Cascade parameters affect the detection in real-time!
    """)
    return


@app.cell
def __controls(mo):
    # Interactive sliders for tuning the HAAR Cascade
    scale_factor = mo.ui.slider(
        start=1.01, stop=1.5, step=0.01, value=1.1, label="Scale Factor"
    )
    min_neighbors = mo.ui.slider(
        start=1, stop=15, step=1, value=5, label="Min Neighbors"
    )

    # Let the user upload a file. 
    # Note: Valid 0.23.0 syntax uses `filetypes` instead of HTML's `accept`.
    image_upload = mo.ui.file(filetypes=["image/*"], label="Upload Image")

    # Group the UI layout
    controls_ui = mo.vstack([
        mo.md("### 1. Tune Parameters"),
        mo.hstack([scale_factor, min_neighbors]),
        mo.md("### 2. Provide an Image"),
        image_upload
    ])
    return image_upload, min_neighbors, scale_factor


@app.cell
def __render_controls():
    # Render the controls in the notebook
    return


@app.cell
def __process_image(cv2, image_upload, min_neighbors, mo, np, scale_factor):
    img = None
    output = mo.md("*Awaiting image input... Upload an image to begin.*")

    # Only process if an image has been uploaded
    if image_upload.value:
        # Decode the uploaded image file
        file_bytes = np.frombuffer(image_upload.value[0].contents, np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

        if img is not None:
            # Convert to grayscale for Haar Cascade detection
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Load the pre-trained HAAR cascade
            cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            face_cascade = cv2.CascadeClassifier(cascade_path)

            # Detect faces using the reactive slider values
            faces = face_cascade.detectMultiScale(
                gray, 
                scaleFactor=scale_factor.value, 
                minNeighbors=min_neighbors.value, 
                minSize=(30, 30)
            )

            # Draw rectangles (Blue, Green, Red) around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 4)

            # OpenCV uses BGR, but the browser (and Marimo) expects RGB
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # In Marimo >= 0.23.0, mo.image natively handles uint8 arrays 
            # without trying to aggressively float-normalize them.
            output = mo.vstack([
                mo.md(f"**Faces detected:** {len(faces)}"),
                mo.image(img_rgb)
            ])

    return


@app.cell
def __display_output():
    # Render the processed image and data to the notebook
    return


if __name__ == "__main__":
    app.run()
