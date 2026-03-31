import cv2
import numpy as np

image = cv2.imread('./robert-katzki-unsplash.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower = np.array([35, 100, 100])
upper = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow('Result', result)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = mask1 + mask2

result = cv2.bitwise_and(image, image, mask=red_mask)   
cv2.imshow('Result', result)


cv2.waitKey(0)
cv2.destroyAllWindows()   