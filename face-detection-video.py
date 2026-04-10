import cv2

# 1. Load the pre-trained HAAR cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Initialize the webcam (0 usually refers to the default built-in camera)
cap = cv2.VideoCapture(0)

print("Press 'q' to quit the video stream.")

while True:
    # 3. Read frame-by-frame from the webcam
    ret, frame = cap.read()
    
    # If a frame was not successfully captured, break the loop
    if not ret:
        print("Failed to grab frame.")
        break

    # 4. Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Detect faces in the current frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 6. Draw green rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 7. Display the resulting frame
    cv2.imshow('Face Detection - Live Video', frame)

    # 8. Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 9. Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
