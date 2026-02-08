# converting an image to grayscale using OpenCV
# import library
import cv2 as cv
from cv2 import cvtColor

img = cv.imread("resources/image.jpg")
img = cv.resize(img, (800,600)) # resizing to 800x600 pixels

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Grayscale Image", gray_img)
cv.waitKey(0) # 0 means wait indefinitely until a key is pressed
cv.destroyAllWindows() #closes all windows