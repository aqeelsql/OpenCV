# how to draw lines and shapes in python

import cv2 as cv
import numpy as np

# draw a canvas
img1 = np.zeros((600,600))
# img2 = np.ones((600,600))
# print("the size of our canvs is ", img1.shape)

# adding colors to the canvas
colored_img = np.zeros((600,600,3), np.uint8)
colored_img[:] = (255,145, 110) #complete img colored

colored_img[150:350, 100:500] = 255, 0, 0 #part of the img colored

#  adding line to the canvas
cv.line(colored_img, (0,0), (300,500), (0,255,0), thickness=10) #line from (0,0) to (300,500) with green color and thickness of 10

# adding rectangle to the canvas
cv.rectangle(colored_img, (50,100), (300, 400), (255,240, 0), cv.FILLED)

# adding circle to the canvas
cv.circle(colored_img, (400,400), 50, (0,0,180), cv.FILLED)

# DDING TEXT TO THE CANVAS
cv.putText(colored_img, 'Hello World', (100, 500), cv.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 3 )
# cv.imshow('black', img1)
# cv.imshow('white', img2)
cv.imshow('colored', colored_img)
cv.waitKey(0)
cv.destroyAllWindows()