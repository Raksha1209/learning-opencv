# done to reduce computational strain
import cv2 as cv
img=cv.imread('PHOTOS/cat.jpg')
cv.imshow('Photo',img)

def rescaleFrame(frame, scale=0.75):
    #works for imgs, vids, and live videos
    width=int(frame.shape[1] * scale) #1 means width
    height=int(frame.shape[0] * scale) #0 means height
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)    



def changeRes(width, height):
    #works only for live videos
    capture.set(3,width) #3 refers width
    capture.set(4,height) #4 refers height
    
    
    
 #reading videos   
capture= cv.VideoCapture('VIDEOS/dog.mp4')
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame)
    
    cv.imshow("Video",frame)
    cv.imshow("Video Resized",frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'): #when pressed D it should stop
            break

capture.release()
cv.destroyAllWindows()
    
    
    
    
    
    
    
cv.waitKey(0)