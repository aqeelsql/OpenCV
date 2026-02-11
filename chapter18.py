# how to change the prespective of an image

import cv2 as cv
import numpy as np 
 
img = cv.imread('resources/warp.jpg')
# print(img.shape)
width, height = 259, 194
# defining points for matrix
# for getting these points see chapter19 
pts1 = np.float32([[54,5], [220,43],[64,180],[218,141]])
pts2 = np.float32([[0,0], [width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts1, pts2)
warp_out = cv.warpPerspective(img, matrix, (width, height))


cv.imshow('original image', img)
cv.imshow('warped image', warp_out)
cv.waitKey(0)
cv.destroyAllWindows()