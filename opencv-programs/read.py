import cv2 as cv

img= cv.imread('PHOTOS/cat.jpg')
cv.imshow('cat',img)
cv.waitKey(0)
#READING IMAGES DONE
#--------------------------------------------------------------------------------------------------
#READING OR CAPTURING VIDEO AS FRAMES
capture= cv.VideoCapture('VIDEOS/dog.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0xFF==ord('d'): #when pressed D it should stop
            break

capture.release()
cv.destroyAllWindows()


#cv.waitkey(0)--->tell opencv to keep the window open until any key is pressed


