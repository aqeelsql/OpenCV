# find coordinates of an image or video

import cv2 as cv
import numpy as np

def find_coordinates(event, x,y, flags, params):
    if event == cv.EVENT_FLAG_LBUTTON:
        # left mouse click
        print(x, '' , y)
        # define or print points on same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + ',' +str(y), (x,y), font, 1, (255,255,0), thickness=2)
        # show the text on image and image itself
        cv.imshow('image', img)
        
# main function
if __name__ == "__main__":
    img = cv.imread('resources/warp.jpg',1)
    # display image
    cv.imshow('image', img)
    # set mouse callback function to find coordinates
    cv.setMouseCallback('image', find_coordinates)
    cv.waitKey(0)
    cv.destroyAllWindows()