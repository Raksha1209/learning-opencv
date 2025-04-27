import cv2 as cv

img = cv.imread('PHOTOS/cats.jpg')
cv.imshow('Cats', img)

# Averaging--if the kernel is 3x3, then avg of all 
# the surrounding boxes is taken , that is considered as the pixel intensity 
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur-same as avg blurring but here each of the pixel is 
#given a weight, so avg of product of those weights
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur--same as averaging, but uses mean
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral-most eff,retains the edges in the img
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)