import cv2
import numpy as np
from pyzbar import pyzbar

def draw_fancy_bounding_box(img, pts, color=(0, 255, 0), thickness=2, bracket_length=20):
    """
    Draws stylized corner brackets instead of a complete rectangle.
    
    :param img: The image to draw on.
    :param pts: A list of the 4 polygon corner points [(x1,y1), (x2,y2)...]
    :param color: BGR color tuple.
    :param thickness: Line thickness.
    :param bracket_length: The length of the bracket leg extending from each corner.
    """
    # Ensure points are integers
    pts = pts.astype(int)

    # Convert the four points into a clean polygon for use
    # pts are usually ordered TL, BL, BR, TR, but might vary slightly.
    # The order doesn't matter much because we loop through adjacencies.
    
    # Need numpy or manual math for vectors. Numpy is cleaner here.
    
    # Step through each corner point
    for i in range(4):
        p_current = pts[i]
        p_prev = pts[(i - 1) % 4] # Previous adjacent point
        p_next = pts[(i + 1) % 4] # Next adjacent point

        # --- Draw line toward the PREVIOUS point ---
        
        # 1. Get the direction vector
        v_prev = p_prev - p_current
        # 2. Get the distance to that point
        dist_prev = np.linalg.norm(v_prev)
        
        # 3. Only draw if the line is long enough
        if dist_prev > bracket_length:
            # 4. Normalize vector and scale by length, add back to start
            end_point_prev = p_current + (v_prev / dist_prev) * bracket_length
            cv2.line(img, tuple(p_current), tuple(end_point_prev.astype(int)), color, thickness)
        else:
            # If the segment is shorter than our bracket, draw the full segment
            cv2.line(img, tuple(p_current), tuple(p_prev), color, thickness)


        # --- Draw line toward the NEXT point ---
        v_next = p_next - p_current
        dist_next = np.linalg.norm(v_next)
        
        if dist_next > bracket_length:
            end_point_next = p_current + (v_next / dist_next) * bracket_length
            cv2.line(img, tuple(p_current), tuple(end_point_next.astype(int)), color, thickness)
        else:
            cv2.line(img, tuple(p_current), tuple(p_next), color, thickness)


def main():
    cap = cv2.VideoCapture(0)
    print("Starting webcam with fancy bounding boxes... Press 'q' to quit.")
    
    last_scanned = ""

    # Setup the live feed window
    cv2.namedWindow("Fancy QR Scanner", cv2.WINDOW_AUTOSIZE)

    while True:
        success, img = cap.read()
        if not success:
            break

        # Flip the image horizontally for a natural 'mirror' view
        img = cv2.flip(img, 1)

        # PyZbar decodes all barcodes and QRs in the frame automatically
        decoded_objects = pyzbar.decode(img)

        # If we found any codes...
        for obj in decoded_objects:
            # 1. Parse the data
            data = obj.data.decode('utf-8')
            
            # 2. Handle the complex bounding box
            # PyZbar gives a simplified rectangle (obj.rect) AND a polygon (obj.polygon).
            # The polygon handles warped/tilted codes better.
            points = obj.polygon
            if len(points) == 4:
                # Convert the polygon object into a usable NumPy array of points
                pts = np.array([tuple(point) for point in points], dtype=np.int32)
                
                # --- APPLY THE FANCY DRAWING FUNCTION ---
                # We specify a thicker, cyan-colored line (color=(255, 255, 0)) for visual pop.
                draw_fancy_bounding_box(img, pts, color=(255, 255, 0), thickness=3, bracket_length=25)

            # 3. Handle the text overlay
            # Position the text slightly above the simplifies 'top-left' rectangle point.
            text_x = obj.rect.left
            text_y = obj.rect.top - 10
            # Ensure text doesn't go off the screen
            if text_y < 20: text_y = obj.rect.top + obj.rect.height + 25

            cv2.putText(img, data, (text_x, text_y),
                        cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 0), 2)

            # 4. Print to console if it's new
            if data != last_scanned:
                print(f"Detected Code: {data}")
                last_scanned = data

        # Display the results
        cv2.imshow("Fancy QR Scanner", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()