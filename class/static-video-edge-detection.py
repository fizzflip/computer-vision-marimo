import cv2

video = cv2.VideoCapture('/home/mrbot/Pictures/V604 MKV - HEVC 4320p 24fps 8bit - AAC2.0.mkv')

frames = []
while video.isOpened():
    ret, frame = video.read()
    if not ret: break
    frames.append(cv2.Canny(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 195, 200))
video.release()

h, w = frames[0].shape
fps = 60
out = cv2.VideoWriter('output_canny_asd.mkv', cv2.VideoWriter_fourcc(*'XVID'), fps, (w, h), isColor=False)
for frame in frames: out.write(frame)
out.release()
