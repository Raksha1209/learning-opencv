import cv2 as cv
import numpy as np
# 2 ways to draw on a img---1]drawing on a given img like cat.png
#                           2] draw on a blank img

blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

#img=cv.imread('PHOTOS/cat.png')
#cv.imshow('Cat',img)

#painting whole img green
blank[:]=0,255,0
#can also give range --->blank[200:300,300:400]
cv.imshow('Green',blank)


#draw a rectangle

cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=-1) #-1 for filled
cv.imshow('Rect',blank)
#draw a circle
cv.circle(blank,(250,250),40,(255,0,0),thickness=-1)
cv.imshow('Circle',blank)
#draw a line
cv.line(blank,(0,0),(250,250),(0,0,255),thickness=3) 
cv.imshow('Line',blank)

#how to write text on image
cv.putText(blank,'Hello, my Name is RawwKshaa',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),2)
cv.imshow('Text',blank)
cv.waitKey(0)