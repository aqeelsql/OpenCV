# basic functions or maiplutions in OpenCV
import cv2 as cv
import numpy as np

img = cv.imread("resources/bird.webp")

# resize image
img = cv.resize(img,(480,250))

# grey_image
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blurred image
blurr_img = cv.GaussianBlur(img,(7,7),0)

# edge detection
edge_img = cv.Canny(img,53,53)

# thickness of lines
mat_kernal = np.ones((3,3), np.uint8)
dilated_img = cv.dilate(edge_img,(mat_kernal), iterations=2)

# erosion(make thinner outline)
ero_img = cv.erode(dilated_img,mat_kernal,iterations=  1)

# cropping an image (use numpy not opencv)
cropped_img = img[50:200, 250:450] # first argument is for length and second is for width
 
cv.imshow('origional_image', img)
# cv.imshow('gray image', gray_img)
# cv.imshow('blurred image', blurr_img)
# cv.imshow('edge image', edge_img)
# cv.imshow('dilated image', dilated_img)
# cv.imshow('erosion image', ero_img)
cv.imshow('cropped image', cropped_img) 
cv.waitKey(0)
cv.destroyAllWindows()

