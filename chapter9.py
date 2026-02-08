# how to capture a webcam

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) # 0 for webcam no.1

# read this webam until end
while(cap.isOpened()):
    # capture frame by frame
    ret, frame = cap.read()
    if ret == True:
        # to display frame
        cv.imshow("Frame", frame)
        #q for quit key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
        break
cap.release()
cv.destroyAllWindows()