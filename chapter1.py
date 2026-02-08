# reading and displaying an image using OpenCV
# import library
import cv2 as cv

img = cv.imread("resources/image.jpg")
cv.imshow("Image", img)
cv.waitKey(0) # 0 means wait indefinitely until a key is pressed

cv.destroyAllWindows()