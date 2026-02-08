# resizing an image using OpenCV
# import library
import cv2 as cv

img = cv.imread("resources/image.jpg")
img = cv.resize(img, (800,600)) # resizing to 800x600 pixels

cv.imshow("Resized Image", img)
cv.waitKey(0) # 0 means wait indefinitely until a key is pressed
cv.destroyAllWindows() #closes all windows