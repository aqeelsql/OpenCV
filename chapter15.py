# resolution of cam
import cv2 as cv

cap = cv.VideoCapture(0)
# resolution for HD(1280x720)
def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)

# resolution for sd(640x480)
def sd_resolution():
    cap.set(3, 640)
    cap.set(4, 480)

# resolution for full hd(1920x1080)
def full_HD_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)
    
# hd_resolution()
# sd_resolution()
full_HD_resolution()

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break   
    
cap.release()
cv.destroyAllWindows()