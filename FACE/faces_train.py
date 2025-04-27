
import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'C:\Users\raksh\Desktop\Youtube-Gesture-Control\OPENCV\FACES\train'

haar_cascade = cv.CascadeClassifier('hard_face.xml')

features = [] #list that will store face regions(images)
labels = [] # List that will store which person the face belongs to (an integer).

def create_train():
    for person in people:
        path = os.path.join(DIR, person) #Full path to the person's folder.
        label = people.index(person)#The index number of the person (e.g., Ben Afflek → 0,

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            if img_array is None:
                continue 
                
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            #scaleFactor=1.1: How much to shrink the image while detecting.
            # minNeighbors=4: How many rectangles should agree to call it a face (higher = stricter).
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training done ---------------')
#convert to array, coz opencv expects arrays not lists
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create() #Local Binary Pattern Histograms.
#A powerful algorithm that recognizes faces based on patterns.

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)       
#there 3 files will appear in directory


#Images ➔ Grayscale ➔ Face Detection ➔ Crop Face ➔ Save Face (features) + Label ➔ Train Recognizer ➔ Save Model

#features	----Cropped face images
#labels	--------Who the face belongs to (index number)
#Haar Cascade----Used to detect faces
#LBPH Recognizer-Used to recognize faces
#Saved Files-----.yml, .npy for future use



