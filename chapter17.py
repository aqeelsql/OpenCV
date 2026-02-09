# joining two images

import cv2 as cv
import numpy as np

img1 = cv.imread('resources/bird.webp')

# stacking same image horizontally
hor_img = np.hstack((img1, img1))
# stacking same image vertically
ver_img = np.vstack((img1, img1))

cv.imshow('horizontal stack', hor_img)
cv.imshow('vertical stack', ver_img)
cv.waitKey(0)
cv.destroyAllWindows()