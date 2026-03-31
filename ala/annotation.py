# import argparse
# import cv2

# # to store the points for region of interest
# roi_pt = []
# roi_pts = []

# # to indicate if the left mouse button is depressed
# is_button_down = False

# def draw_rectangle(event, x, y, flags, param):
#     global roi_pt, is_button_down

#     if event == cv2.EVENT_MOUSEMOVE and is_button_down:
#         global image_clone, image

#         # get the original image to paint the new rectangle
#         image = image_clone.copy()

#         # draw new rectangle
#         cv2.rectangle(image, roi_pt[0], (x,y), (0, 255, 0), 2)

#     if event == cv2.EVENT_LBUTTONDOWN:
#         # record the first point
#         roi_pt = [(x, y)]
#         is_button_down = True

#     # if the left mouse button was released
#     elif event == cv2.EVENT_LBUTTONUP:        
#         roi_pt.append((x, y))     # append the end point
#         roi_pts.append(roi_pt)
#         # ======================
#         # print the bounding box
#         # ======================
#         # in (x1,y1,x2,y2) format
#         print(roi_pt)                  

#         # in (x,y,w,h) format
#         bbox = (roi_pt[0][0],
#                 roi_pt[0][1],
#                 roi_pt[1][0] - roi_pt[0][0],
#                 roi_pt[1][1] - roi_pt[0][1])
#         print(bbox)

#         # button has now been released
#         is_button_down = False

#         # draw the bounding box
#         cv2.rectangle(image, roi_pt[0], roi_pt[1], (0, 255, 0), -1)
#         cv2.imshow("image", image)

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required = True, help = "Path to image")
# args = vars(ap.parse_args())

# # load the image
# image = cv2.imread(args["image"])

# # reference to the image
# image_clone = image

# # setup the mouse click handler
# cv2.namedWindow("image")
# cv2.setMouseCallback("image", draw_rectangle)

# # loop until the 'q' key is pressed
# while True:
#     # display the image 
#     cv2.imshow("image", image)

#     # wait for a keypress
#     key = cv2.waitKey(1)
#     if key == ord("q"):
#         print("ROIs", roi_pts)
#         # with open(f'{args["image"]}_roi_pt.txt', 'w+') as f:
#         #     f.write(roi_pt)
#         break

# # close all open windows
# cv2.destroyAllWindows()

import argparse
import cv2

roi_pt = []
roi_pts = []
is_button_down = False

# drawing mode: "rect", "circle", "line"
draw_mode = "rect"

def draw_shape(event, x, y, flags, param):
    global roi_pt, is_button_down
    global image, image_clone, draw_mode

    # while dragging mouse
    if event == cv2.EVENT_MOUSEMOVE and is_button_down:
        image = image_clone.copy()

        if draw_mode == "rect":
            cv2.rectangle(image, roi_pt[0], (x, y), (0,255,0), 2)

        elif draw_mode == "circle":
            cx, cy = roi_pt[0]
            radius = int(((x-cx)**2 + (y-cy)**2)**0.5)
            cv2.circle(image, (cx, cy), radius, (255,0,0), 2)

        elif draw_mode == "line":
            cv2.line(image, roi_pt[0], (x, y), (0,0,255), 2)

    if event == cv2.EVENT_LBUTTONDOWN:
        roi_pt = [(x, y)]
        is_button_down = True

    elif event == cv2.EVENT_LBUTTONUP:
        roi_pt.append((x, y))
        roi_pts.append((draw_mode, roi_pt))
        print(draw_mode, roi_pt)

        is_button_down = False
        image_clone[:] = image

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image_clone = image.copy()

cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_shape)

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # change drawing mode
    if key == ord("r"):
        draw_mode = "rect"
        print("Mode: rectangle")

    elif key == ord("c"):
        draw_mode = "circle"
        print("Mode: circle")

    elif key == ord("l"):
        draw_mode = "line"
        print("Mode: line")

    elif key == ord("q"):
        print("ROIs:", roi_pts)
        break

cv2.destroyAllWindows()
