 # saving video using opencv
import cv2 as cv

cap = cv.VideoCapture('resources/video.mov')

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("Out_video.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height),isColor=False)

while (True):
    (ret, frame) = cap.read()
    (thresh, binary) = cv.threshold(frame, 127, 255, cv.THRESH_BINARY)
    # to show binary video
    if ret == True:
        resize_frame = cv.resize(binary, (800, 600))
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