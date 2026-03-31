import cv2

def main():
    # Initialize the webcam (0 is usually the default, built-in camera)
    cap = cv2.VideoCapture(0)

    # Initialize OpenCV's built-in QR Code detector
    detector = cv2.QRCodeDetector()

    print("Starting webcam... Press 'q' to quit.")

    # Keep track of the last scanned code to avoid spamming the console
    last_scanned = ""

    while True:
        # Capture frame-by-frame
        success, img = cap.read()
        
        if not success:
            print("Failed to access the webcam.")
            break

        # Detect and decode the QR code in the current frame
        data, bbox, _ = detector.detectAndDecode(img)
        
        # If a QR code is found (bbox is not None) and it contains data
        if bbox is not None and data:
            # Draw a bounding box around the QR code
            for i in range(len(bbox[0])):
                # Get the current point and the next point to draw a line
                pt1 = tuple(map(int, bbox[0][i]))
                pt2 = tuple(map(int, bbox[0][(i+1) % len(bbox[0])]))
                cv2.line(img, pt1, pt2, color=(0, 255, 0), thickness=2)
            
            # Display the decoded text directly on the video feed
            cv2.putText(img, data, (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # Print to console only if it's a new QR code to prevent console spam
            if data != last_scanned:
                print(f"Detected QR Code: {data}")
                last_scanned = data

        # Display the live feed window
        cv2.imshow("Live QR Code Scanner", img)
        
        # Break the loop and close the window when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up and release the webcam
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
