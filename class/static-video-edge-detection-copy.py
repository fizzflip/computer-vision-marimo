import cv2

video = cv2.VideoCapture('/home/mrbot/Documents/devenvs/marimo/samples/videos/PXL_20260402_181749999.mp4')

frames = []
while video.isOpened():
    ret, frame = video.read()
    if not ret: break
    converted_frame = cv2.cvtColor(cv2.resize(frame, (720, 1280)), cv2.COLOR_BGR2GRAY)
    edged_frame = cv2.Canny(converted_frame, 20, 50)
    cv2.imshow("Video", edged_frame)
    cv2.waitKey(0)
video.release()

# print(frames[0])
# h, w = frames[0].shape
# fps = 60
# out = cv2.VideoWriter('output_canny_asd.mkv', cv2.VideoWriter_fourcc(*'XVID'), fps, (w, h), isColor=False)
# for frame in frames: out.write(frame)
out.release()
