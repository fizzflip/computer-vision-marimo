import marimo

__generated_with = "0.19.5"


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import cv2
    return cv2, mo, np


@app.cell
def _():
    height, width, channels = 500, 500, 3
    return channels, height, width


@app.cell
def _():
    # frame = np.zeros((height, width, channels), dtype=np.uint8)
    # base_frame = np.random.randint(0, 256, (height, width, channels), dtype=dtype)
    return


@app.cell
def _(channels, cv2, height, np, width):
    frames = []
    for i in range(0, 500, 10):
        frame = np.zeros((height, width, channels), dtype=np.uint8)

        if ((i - 100) < 100) or ((100 - i) < 100):
            cv2.circle(frame, (i, 100), 10, (0, 0, 255), -1)
            cv2.circle(frame, (100, i), 10, (0, 255, 0), -1)
        else:
            cv2.circle(frame, (100, i), 10, (0, 0, 255), -1)
            cv2.circle(frame, (i, 100), 10, (0, 255, 0), -1)
        
    
    
    
        # cv2.circle(frame, (i, 100), 50, (0, 0, 255), -1)
        # cv2.circle(frame, (100, i), 50, (255, 0, 0), -1)
        # cv2.circle(frame, (i, i), 50, (0, 255, 0), -1)
        frames.append(frame)
    return (frames,)


@app.cell
def _(cv2, frames, height, width):
    output_path = "./output_video.mp4"
    fps = 30  # Frames per second
    frame_size = (width, height) # (width, height)

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, frame_size)

    for fr in frames:
        out.write(fr)

    out.release()   
    return


@app.cell
def _(mo):
    mo.video("./output_video.mp4")
    return


if __name__ == "__main__":
    app.run()
