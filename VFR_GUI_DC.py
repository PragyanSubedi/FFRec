import numpy as np
import cv2
import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk
import urllib
import sqlite3
import ttk
import tkMessageBox
import os

#Global variables
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 0, 0)
fontColor1 = (0, 0, 255)
# global lbl
#create username
# lbl_username = tk.Label(root, text="Username", bg="#0D7E50")
# ent_username = tk.Entry(root)
#
# #pack username
# lbl_username.grid(row=5, column=0)
# ent_username.grid(row=6, column=0)
#
# #basic enter for password
# lbl_password = tk.Label(root, text="Password", bg="#0D7E50")
# ent_password = tk.Entry(root, show="*")
#
# #pack password
# lbl_password.grid(row=5, column=1,sticky = N)
# ent_password.grid(row=6, column=1)
# btn = Tkinter.Button(window, text="Sign up", command=question)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainer/trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascadePath);

sampleNum = 0
Id=0

url='http://192.168.0.109:8080/shot.jpg'

#Set up GUI
root = tk.Toplevel()
root.geometry("1280x800")
#Makes main window
root.wm_title("Floating Faces")
root.config(background="#d9d9d9")

#Graphics window
imageFrame = tk.Frame(root, width=200, height=600)
imageFrame.grid(row=0, column=0, padx=70, pady=100)
# Button(root,text=tk.Frame = tk.LabelFrame"Submit").grid(row=3)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)


#for trainer
def getImagesAndLabels(path):
    # Get all file path
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    # Initialize empty face sample
    faceSamples = []

    # Initialize empty id
    ids = []

    # Loop all the file path
    for imagePath in imagePaths:

        # Get the image and convert it to grayscale
        PIL_img = Image.open(imagePath).convert('L')

        # PIL image to numpy array
        img_numpy = np.array(PIL_img, 'uint8')

        # Get the image id
        id = int(os.path.split(imagePath)[-1].split(".")[1])

        # Get the face from the training images
        faces = detector.detectMultiScale(img_numpy)

        # Loop for each face, append to their respective ID
        for (x, y, w, h) in faces:
            # Add the image to face samples
            faceSamples.append(img_numpy[y:y + h, x:x + w])

            # Add the ID to IDs
            ids.append(id)

    # Pass the face array and IDs array
    return faceSamples, ids

#for dataset creator
def insertOrUpdate(Name):
    conn = sqlite3.connect("Faces1.0.db")
    with conn:
        cur=conn.cursor()
        cur.execute("INSERT INTO People(Name) VALUES ('"+ Name +"');")
        max_id = cur.lastrowid
        Id= max_id
    cmd = "SELECT * FROM People WHERE ID="+str(Id)
    cursor = conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        #str(sname) = testname
        cmd = "UPDATE people SET Name=' " + "testname" + " ' WHERE ID=" + str(Id)
    else:
        #str(sname) = testname
        cmd = "INSERT INTO people(ID,Name) Values(" + str(Id) + ",' " + "testname" + " ' )"
    conn.execute(cmd)
    conn.commit()
    conn.close()
    return max_id
Id = insertOrUpdate("testname")

#to run on clicking the button "Train"
def createDataset(event):
    # global lbl
    # # change text
    lbl.config(text="Your face has been saved. You can now close this window.")

    global sampleNum
    sampleNum=0

    while(True):
        imgResp = urllib.urlopen(url)
        # change into bytearray of unsigned integer type
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
        # Decode numpy array to opencv2 image
        img = cv2.imdecode(imgNp, -1)
        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            sampleNum= sampleNum + 1
            cv2.imwrite("Faces database/face-" + "testname" + "." + str(Id) + "."+ str(sampleNum)+".jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(cv2image, (x - 50, y - 50), (x + w + 50, y + h + 50), (0, 255, 0), 2)
            # break if the sample number is more than 5
        if sampleNum > 5:
            break

    # Trainer
    # # Create Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Get the faces and IDs
    faces, ids = getImagesAndLabels('Faces database/')

    # Train the model using the faces and IDs
    recognizer.train(faces, np.array(ids))

    # Save the model into trainer.yml
    # with open('trainer.yml', "a") as recognizer:
    recognizer.write('trainer/trainer.yml')
    return
# Quits the TkInter app when called
def quit_app():
    root.quit()

# Opens a message box when called
def show_about(event=None):
    tkMessageBox.showwarning(
        "About",
        "This Awesome Program was Made in 2017"
    )

# Create the menu object
the_menu = Menu(root)

# ----- FILE MENU -----

# Create a pull down menu that can't be removed
file_menu = Menu(the_menu, tearoff=0)

# Add items to the menu that show when clicked
# compound allows you to add an image
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")

# Add a horizontal bar to group similar commands
file_menu.add_separator()

# Call for the function to execute when clicked
file_menu.add_command(label="Quit", command=quit_app)

# Add the pull down menu to the menu bar
the_menu.add_cascade(label="File", menu=file_menu)

lbl = Label(root, text="Please set up your face in the database", bg="#00394d")
lbl.grid(row=0, column=30, pady=100, padx=20)

creatorButton2= Button(root, text='Set it up', activebackground='white',foreground="ivory2",
                background="gray23",
                font="Helvetica 14 bold italic",
                borderwidth=7)
creatorButton2.grid(row=0,column=11)
creatorButton = Button(root, text="Set it Up!")
creatorButton.bind("<Button-1>", createDataset)
creatorButton.grid(row=0, column=10)

#shows video frame
def showFrame():
    imgResp = urllib.urlopen(url)

    # change into bytearray of unsigned integer type
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)

    # Decode numpy array to opencv2 image
    img = cv2.imdecode(imgNp, -1)
    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(cv2image, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(cv2image, (x - 50, y - 50), (x + w + 50, y + h + 50), (0, 255, 0), 2)

    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(5, showFrame)

root.config(menu=the_menu)
showFrame()  #Display loop

root.mainloop()  #Starts GUI