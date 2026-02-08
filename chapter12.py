# setting brightnss, height and width of frame

import cv2 as cv

cap = cv.VideoCapture(0)

cap.set(10, 50) #10 is the key for brightness and 50 means 50% brightness
cap.set(3, 1920) # 3 is the key for width
cap.set(4, 1080) # 4 is the key for height
while(True):
    ret, frame = cap.read()
    if ret ==True:
        cv.imshow("Frame", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
        
cap.release()
cv.destroyAllWindows()