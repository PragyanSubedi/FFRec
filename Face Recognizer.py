import numpy as np
import cv2
import sqlite3
import urllib
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (0, 0, 255)

url='http://192.168.1.100:8080/shot.jpg'
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('images/test.jpg', cv2.IMREAD_COLOR)

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


#font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
# while True:
#     imgResp=urllib.urlopen(url)
#     #change into bytearray of unsigned integer type
#     imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
#     #Decode numpy array to opencv2 image
#     img=cv2.imdecode(imgNp,-1)
#     locy = int(img.shape[0] / 2)  # the text location will be in the middle
#     locx = int(img.shape[1] / 2)  # of the frame for this example

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray, 1.2,5)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)
    Idu, conf = recognizer.predict(gray[y:y+h, x:x+w])

    profile = getProfile(Idu)
    if(profile!=None):
        cv2.putText(img, str(profile[1]), (x,y+h+30),fontFace, fontScale, fontColor)
        cv2.putText(img, str(profile[2]), (x, y + h + 60), fontFace, fontScale, fontColor)
        cv2.putText(img, str(profile[3]), (x, y + h + 90), fontFace, fontScale, fontColor)
        cv2.putText(img, str(profile[4]), (x, y + h + 120), fontFace, fontScale, fontColor)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()