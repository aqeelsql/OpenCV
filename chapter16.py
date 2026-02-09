# saving HD Video
import cv2 as cv

cap = cv.VideoCapture(0)

# resolution for full hd(1920x1080)
def full_HD_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)
    
# hd_resolution()
# sd_resolution()
full_HD_resolution()
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("HD video.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
while (True):
    (ret, frame) = cap.read()
    # to show binary video
    if ret == True:
        out.write(frame)
        cv.imshow("HD Video", frame)
        # to quit with q key
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break  
    
cap.release()
cv.destroyAllWindows()