import cv2
from pyzbar import pyzbar

def main():
    cap = cv2.VideoCapture(0)
    print("Starting webcam with PyZbar... Press 'q' to quit.")
    
    last_scanned = ""

    while True:
        success, img = cap.read()
        if not success:
            break

        # PyZbar decodes all barcodes and QRs in the frame automatically
        decoded_objects = pyzbar.decode(img)

        for obj in decoded_objects:
            # PyZbar returns data as bytes, so we decode it to a string
            data = obj.data.decode('utf-8')
            
            # Draw a bounding box around the detected QR code
            points = obj.polygon
            if len(points) == 4:
                pts = [tuple(point) for point in points]
                for i in range(4):
                    cv2.line(img, pts[i], pts[(i+1)%4], (0, 255, 0), 3)

            # Display the text on the screen
            cv2.putText(img, data, (obj.rect.left, obj.rect.top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # Print to console if it's new
            if data != last_scanned:
                print(f"Detected Visual QR Code: {data}")
                last_scanned = data

        cv2.imshow("Robust Visual QR Scanner", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
