#gradients and edges are completely diff frm mathematical point of view
#Where the color changes slowly → gradient is small.
#Where the color changes suddenly → gradient is big.

#An edge is where there’s a strong gradient.

#we had seen canny

import cv2 as cv
import numpy as np

img = cv.imread('PHOTOS/cat.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#🧭 Sobel → “Tell me the direction of edges — vertical, horizontal, etc.”

#⚡ Laplacian → “Just give me the edges, fast.”



# Laplacian-detects edges in all directions at once
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel-finds gardient in a specific direction
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)