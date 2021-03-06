import numpy as np
import cv2
import Tkinter as tk
from Tkinter import *
import Image, ImageTk
import urllib
import sqlite3
import ttk
import tkMessageBox
from face_recognizer import recognizeFace
from dataset_creator import datasetCreate

#Global variables
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
fontColor = (255, 0, 0)
fontColor1 = (0, 0, 255)
sampleNum =0
#url='http://192.168.0.109:8080/shot.jpg'

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainer/trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascadePath);

#Set up GUI
root = tk.Tk()
root.geometry("1280x800")
#Makes main window
root.wm_title("Floating Faces")
root.config(background="#00394d")

#Graphics window
imageFrame = tk.Frame(root, width=200, height=600)
imageFrame.grid(row=0, column=0, padx=70, pady=100)
# Button(root,text=tk.Frame = tk.LabelFrame"Submit").grid(row=3)

#Capture video frames
lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)


# Quits the TkInter app when called
def quit_app():
    root.quit()


# Opens a message box when called
def show_about(event=None):
    tkMessageBox.showwarning(
        "About",
        "This Awesome Program was Made in 2016"
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
        cmd = "UPDATE people SET Name=' " + str(sname) + " ' WHERE ID=" + str(Id)
    else:
        cmd = "INSERT INTO people(ID,Name) Values(" + str(Id) + ",' " + str(sname) + " ' )"
    conn.execute(cmd)
    conn.commit()
    conn.close()
    return max_id
## VIDEO FEED ##
def createFrame():

    cv2image = datasetCreate()

#Slider window (slider controls stage position)
#sliderFrame = tk.Frame(root, width=1000, height=200)
#sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

root.config(menu=the_menu)
createFrame()  #Display loop
root.mainloop()  #Starts GUI
