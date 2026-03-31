import cv2

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left click at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right click at ({x}, {y})")

    

cap = cv2.VideoCapture("/home/mrbot/Documents/devenvs/marimo/Class/Test Jellyfin 1080p AVC 3M.mp4")

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", on_mouse)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video", frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()