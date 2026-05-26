import cv2

video = cv2.VideoCapture("./test-jellyfin-basic.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("./test-jellyfin-canny.mp4", fourcc, 60, (500, 500))

while True:
    ret, frame = video.read()
    if not ret: break
    frame = cv2.resize(frame, (500, 500))
    frame = cv2.cvtColor(cv2.Canny(frame, 50, 150), cv2.COLOR_GRAY2RGB)    
    out.write(frame)
out.release()
video.release()


