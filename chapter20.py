# splitting videos into frames

import cv2 as cv

cap = cv.VideoCapture('resources/video.mov') 

frameNo = 0

while(True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f'resources/frames/frame_{frameNo}.jpg', frame)
    else:
        break    
        
    frameNo = frameNo+1
cap.release()
cv.destroyAllWindows()    