import cv2 as cv
import numpy as np

img=cv.imread('PHOTOS/cat.jpg')

cv.imshow('cat',img)

#translation--shifting an image along x and y axis
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

#  -y----up
#   y----down
#   x---right
#  -x---left
translated=translate(img,100,100)
#transform the img by moving 100 pixels right, and 100 px down
cv.imshow('Translated',translated)

#rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    
    if rotPoint is None:
        rotPoint=(width//2,height//2)
        
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-45)
cv.imshow('Rotated',rotated)

#RESIZING
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#FLIPPING
#0-flip along x axis,1-flip along y axis, -1-->both vertically and horizontlly
fliped=cv.flip(img,0)
cv.imshow('Flip',fliped)

#cropping
cropped= img[200:400,300:400]
cv.imshow('Cropped',cropped)








cv.waitKey(0)
























