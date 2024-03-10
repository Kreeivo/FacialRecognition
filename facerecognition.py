import numpy as np
import cv2
import time

a = {1: cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml'),
     2: cv2.CascadeClassifier('Cascades/haarcascade_eye.xml'),
     3: cv2.CascadeClassifier('Cascades/haarcascade_frontalcatface.xml')}

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

def faceRecog():
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, -1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,     
            scaleFactor=1.2,
            minNeighbors=5,     
            minSize=(20, 20)
        )
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]  
        cv2.imshow('video',img)
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break
    cap.release()
    cv2.destroyAllWindows()
    
# ------- User Interaction Below ------- # 

userChoice = int(input("Enter a choice of facial recognition \n 1. Default Recognition \n 2. Recognition with Eyes \n 3. Recognition with some random one that i dont know what it does. \n "))


print("Option ", userChoice,  "Selected")
faceCascade = a[userChoice]
time.sleep(3)
print("Initialisting Option " , userChoice)
time.sleep(3)
faceRecog()




