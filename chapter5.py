# writig an image using opencv
import cv2 as cv

img = cv.imread("resources/image.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite("resources/gray_image.jpg", gray)
(thresg, b_w) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
cv.resize(b_w, (400, 600))
cv.imwrite("resources/binary_image.jpg", b_w)