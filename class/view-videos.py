import cv2
video = cv2.VideoCapture('/home/mrbot/Documents/devenvs/marimo/samples/videos/test-jellyfin-basic.mp4')
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        print("Can't receive frame, exiting ...")
        break

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow(frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()