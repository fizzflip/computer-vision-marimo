import cv2
import numpy as np

image = cv2.imread('flower-image.jpg')

# Show 
# cv2.imshow('Final', image)

# cropped = image[40:100, 100:200]
# cv2.imshow('Image', cropped)

# Resized
# resized = cv2.resize(image, (100,100))
# cv2.imshow("asd", resized)

# Draw
# img_copy = image.copy()

# cv2.putText(img_copy, "Hwllo", (50,50), cv2.FONT_HERSHEY_COMPLEX, 10, (255,0,0), 10)
# cv2.imshow("asdasd", img_copy)

# 
# bright_img = cv2.convertScaleAbs(image, alpha=2, beta=-100)

# br_img = cv2.add(image, -50)

image2 = cv2.imread('flower-image-2.jpg')

# new_img = cv2.subtract(image, image2)

# print(image.shape, image2.shape)

# changed = cv2.divide(image2, 5)

# converted = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)


cv2.imshow('asd', converted)
cv2.waitKey(0)
cv2.destroyAllWindows()