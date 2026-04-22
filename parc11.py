import numpy as np
import cv2
import matplotlib.pyplot as plt

# 1. Load the image
img = cv2.imread('./samples/images/girl-straight-viewer.jpg')
# Convert BGR to RGB for accurate matplotlib display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 2. Create an empty mask
# The mask will store the segmentation results (0=BG, 1=FG, 2=Probable BG, 3=Probable FG)
mask = np.zeros(img.shape[:2], np.uint8)

# 3. Allocate memory for the internal GMM models used by GrabCut
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

# 4. Define the bounding box (x, y, width, height)
# Ensure this tightly wraps your subject!
rect = (50, 50, 450, 290) 

# 5. Run the GrabCut algorithm
# parameters: image, mask, bounding box, bg model, fg model, iterations, mode
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

# 6. Interpret the mask
# GrabCut modifies 'mask'. We want to change values 0 and 2 (definite/probable background) to 0, 
# and values 1 and 3 (definite/probable foreground) to 1.
mask_binary = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# 7. Apply the binary mask to the original image
# We add a new axis to the mask so it can multiply against the 3 color channels (RGB)
foreground = img_rgb * mask_binary[:, :, np.newaxis]

# 8. Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Image with Bounding Box")
# Draw a rectangle just to visualize where we placed it
img_rect = img_rgb.copy()
cv2.rectangle(img_rect, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (255, 0, 0), 2)
plt.imshow(img_rect)

plt.subplot(1, 2, 2)
plt.title("Extracted Foreground")
plt.imshow(foreground)
plt.show()
