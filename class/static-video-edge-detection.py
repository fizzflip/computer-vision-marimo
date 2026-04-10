import cv2

video = cv2.VideoCapture('/home/mrbot/Documents/devenvs/marimo/samples/videos/PXL_20260402_181749999.mp4')

print(video)

frames = []
while video.isOpened():
    ret, frame = video.read()
    if not ret: break
    frames.append(cv2.Canny(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 195, 200))
video.release()

print(frames[0])
h, w = frames[0].shape
fps = 60
out = cv2.VideoWriter('output_canny_asd.mkv', cv2.VideoWriter_fourcc(*'XVID'), fps, (w, h), isColor=False)
for frame in frames: out.write(frame)
out.release()
