# converting an image int b&w
import cv2 as cv


img = cv.imread("resources/image.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(threash, b_w) = cv.threshold(gray, 127, 155, cv.THRESH_BINARY)
cv.imshow("B&W Image", b_w)
cv.waitKey(0)
cv.destroyAllWindows()