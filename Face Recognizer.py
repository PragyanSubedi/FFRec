import numpy as np
import cv2
import sqlite3

fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (0, 0, 255)


detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
im = cv2.imread('download.jpeg', cv2.IMREAD_COLOR)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path= 'dataSet'

def getProfile(Id):
    conn=sqlite3.connect("Faces1.0.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

locy = int(im.shape[0]/2) # the text location will be in the middle
locx = int(im.shape[1]/2) #           of the frame for this example

#font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)

gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray, 1.2,5)
for(x,y,w,h) in faces:
    cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
    Id, conf = recognizer.predict(gray[y:y+h,x:x+w])

    profile = getProfile(Id)
    if(profile!= None):
        cv2.putText(im, str(profile[1]), (x,y+h+30),fontFace, fontScale, fontColor)
        cv2.putText(im, str(profile[2]), (x, y + h + 60), fontFace, fontScale, fontColor)
        cv2.putText(im, str(profile[3]), (x, y + h + 90), fontFace, fontScale, fontColor)
        cv2.putText(im, str(profile[4]), (x, y + h + 120), fontFace, fontScale, fontColor)
    cv2.imshow('im',im)
cv2.waitKey(0)
cv2.destroyAllWindows()