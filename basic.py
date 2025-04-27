import cv2 as cv

img= cv.imread('PHOTOS/cat.jpg')
cv.imshow('cat',img)

#converting to gray scale
#Back in the old-school days, when OpenCV was first developed (early 2000s), 
# it was built using C/C++, and many older camera drivers, image libraries, 
# and standards stored images in BGR order — not RGB.
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur img--to reduce the noise in an image
blur= cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT) #(3,3)-->if incresed , more blurred it looks
cv.imshow('Blur',blur)

#edge cascade--> finds the edges
canny=cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

#dilating image--type of img processing where white parts of img grow or thicken, white lines thicken
dilated = cv.dilate(canny, (5,5), iterations=3)
cv.imshow("Dilated",dilated)

#eroding-opp of dilating, thins out the edge
eroded = cv.erode(img, (5,5), iterations=3)
cv.imshow("Eroded",eroded)

#resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#cv.INTER_AREA--for downscaling, LINEAR--for upscaling, CUBIC-for sharp results
cv.imshow("resized",resized)

#cropping
#imgs are like arrays
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)


cv.waitKey(0)