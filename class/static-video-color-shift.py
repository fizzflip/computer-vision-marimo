import cv2


def analyse_frame_color(frame):
    resized_frame = cv2.resize(frame, (100, 100), interpolation = cv2.INTER_AREA)
    # hsv_frame = 

video = cv2.VideoCapture('/home/mrbot/Documents/devenvs/marimo/samples/videos/test-jellyfin-basic.mp4')

frames = []
while video.isOpened():
    ret, frame = video.read()
    if not ret: break

    frames.append(cv2.Canny(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 195, 200))
video.release()

h, w = frames[0].shape
fps = 60
out = cv2.VideoWriter('output_color_over.mkv', cv2.VideoWriter_fourcc(*'XVID'), fps, (w, h), isColor=False)
for frame in frames: out.write(frame)
out.release()
