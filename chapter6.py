# reading a video using opencv
import cv2 as cv

cap = cv.VideoCapture('resources/video.mov')
if(cap.isOpened() == False):
    print("Error in loading video")
    
# reading and playing video
while(cap.isOpened()):
    ret, frame = cap.read()
    # to show video
    if ret == True:
        resize_frame = cv.resize(frame, (640, 480)) 
        cv.imshow("video", resize_frame)
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()