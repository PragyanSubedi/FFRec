import numpy as np
import cv2
import sqlite3
import urllib
from Dataset creator __import__(sampleNum)

fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 0, 0)
# for record not found case
fontColor1 = (0, 255, 255)

url='http://192.168.1.180:8080/shot.jpg'
sconf=100
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img = cv2.imread('images/download.jpeg', cv2.IMREAD_COLOR)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
# path= 'dataSet'

def getProfile(Id):
    conn=sqlite3.connect("Faces1.0.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

def getconf(conf):
    con=sqlite3.connect("Lowest_conf.db")
    cmd1="INSERT INTO CONFIDENCE(smallest_conf) Values "+str(conf)+""
    cursor=con.execute(cmd1)
    c=None
    for row in cursor:
        c=row
    con.commit()
    con.close()
    return c



#font = cv2.InitFont(cv2.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    imgResp=urllib.urlopen(url)
    #change into bytearray of unsigned integer type
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    #Decode numpy array to opencv2 image
    img=cv2.imdecode(imgNp,-1)

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        # sampleNum= sampleNum+1
        Idu, conf = recognizer.predict(gray[y:y+h, x:x+w])
        #for
        if(conf<sconf):
            sconf=conf
            c=getconf(sconf)
            cv2.putText(img,str(conf), (x, y + h + 120 ), fontFace, fontScale, fontColor1)
            pass
        if (conf<80):
            cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)
            profile = getProfile(Idu)
            if(profile!=None):
                cv2.putText(img, str(profile[1]), (x,y+h+30),fontFace, fontScale, fontColor)
                cv2.putText(img, str(profile[2]), (x, y + h + 60), fontFace, fontScale, fontColor)
                cv2.putText(img, str(profile[3]), (x, y + h + 90), fontFace, fontScale, fontColor)
                #cv2.putText(img, str(profile[4]), (x, y + h + 120), fontFace, fontScale, fontColor)
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 225), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            # cv2.putText(img,"Not Found", (x, y + h + 30 ), fontFace, fontScale, fontColor1)
    cv2.imshow('frame', img)
    # cv2.waitKey(2000)
    if ord('q') == cv2.waitKey(1):
        break
cv2.destroyAllWindows()