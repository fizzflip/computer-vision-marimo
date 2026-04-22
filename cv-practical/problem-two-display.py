import cv2

video = cv2.VideoCapture("./test-jellyfin-basic.mp4")

while True:
    ret, frame = video.read()
    if not ret: break
    cv2.imshow('video', frame)
    cv2.waitKey(60)

cv2.destroyAllWindows()
video.release()


