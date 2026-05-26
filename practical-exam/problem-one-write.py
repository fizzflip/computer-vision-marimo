import cv2

img = cv2.imread('./sample-image.jpg')

# Resized image
img = cv2.resize(img, (1600, 900))

img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imwrite(img_gray)