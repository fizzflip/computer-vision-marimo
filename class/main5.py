import cv2

# Store circle centers
circles = [ (500,500) ]

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))

# Open video (0 = webcam, or replace with video path)
cap = cv2.VideoCapture(0)

cv2.namedWindow("Video")
cv2.setMouseCallback("Video", draw_circle)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Draw all stored circles
    for (x, y) in circles:
        cv2.circle(frame, (x, y), 15, (0, 255, 0), 2)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(30) & 0xFF
    if key == 27:  # ESC to quit
        break
    elif key == ord('c'):  # press 'c' to clear circles
        circles.clear()

cap.release()
cv2.destroyAllWindows()
