 # writing videos from cam
import cv2 as cv

cap = cv.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("cam_video.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while (True):
    (ret, frame) = cap.read()
    # to show binary video
    if ret == True:
        resize_frame = cv.resize(frame, (800, 600))
        out.write(frame)
        cv.imshow("binaryvideo", resize_frame)
        # to quit with q key
        if cv.waitKey(1) & 0xFF ==ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv.destroyAllWindows()