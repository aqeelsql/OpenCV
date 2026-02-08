# converting video into gray and b&w

import cv2 as cv

cap = cv.VideoCapture('resources/video.mov')

while (True):
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # to show gray video
    if ret == True:
        resize_frame = cv.resize(grayframe, (800,600))
        cv.imshow("grayvideo", resize_frame)
        # to quit with q key
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break
    
cap.release()
cv.destroyAllWindows()