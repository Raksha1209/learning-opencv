#color-spaces==spaces of colors, a system of representing
#an array of pixel colours--rgb,bgr
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('PHOTOS/cat.jpg')
cv.imshow('cat', img)

# plt.imshow(img) #you'll get tto see how  bgr image looks
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV(how humans perceive the color)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR(opencv uses this) to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)