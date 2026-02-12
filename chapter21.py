# how to detect specific colors inside an image using OpenCV

import cv2 as cv
import numpy as np
# img = cv.imread('resources/bird.webp')

# convert the image to HSV(hue, saturtion,value) color space
# hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# sliders
def slider():
    pass

path = "resources/bird.webp"
cv.namedWindow('Bars')
cv.resizeWindow('Bars', 640, 240)
cv.createTrackbar('HUE Min', 'Bars', 0, 179, slider)    
cv.createTrackbar('Hue Max', 'Bars', 179, 179, slider) 
cv.createTrackbar('Sat Min', 'Bars', 0, 255, slider)    
cv.createTrackbar('Sat Max', 'Bars', 255, 255, slider) 
cv.createTrackbar('Value Min', 'Bars', 0, 255, slider)    
cv.createTrackbar('Value Max', 'Bars',255, 255, slider)    
    
img = cv.imread(path)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

while True:
    img = cv.imread(path)
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hue_min = cv.getTrackbarPos('HUE Min', 'Bars')
    hue_max = cv.getTrackbarPos('Hue Max', 'Bars')
    sat_min = cv.getTrackbarPos('Sat Min', 'Bars')
    sat_max = cv.getTrackbarPos('Sat Max', 'Bars')
    val_min = cv.getTrackbarPos('Value Min', 'Bars')
    val_max = cv.getTrackbarPos('Value Max', 'Bars')
    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)
    
    # to see changes inside image
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask_img = cv.inRange(hsv_img, lower, upper)
    out_img = cv.bitwise_and(img, img, mask=mask_img)
    # cv.imshow('Original Image', img)
    # cv.imshow('HSV Image', hsv_img)
    cv.imshow('Mask Image', mask_img)
    cv.imshow('Output Image', out_img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()