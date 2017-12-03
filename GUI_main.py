#!/usr/bin/python
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
from tkFileDialog import askopenfilename

url='http://192.168.1.180:8080/shot.jpg'
root = tk.Tk()
root.geometry("1280x700")
#Makes main window
root.wm_title("Floating Faces")
root.config(background="#0D7E50")

# #Graphics window
# imageFrame = tk.Frame(root, width=200, height=600)
# imageFrame.grid(row=0, column=0, padx=70, pady=100)
#
# def question():
#     username=ent_username.get()
#     password = ent_password.get()
#
#     if (username!=None and password!=None):
#         setupDatabase()
#     else:
#         print "Enter usernaame"
def setupDatabase():

    # execfile("VFR_GUI_DC.py")
    import VFR_GUI_DC

def chooseDir():
    name = askopenfilename()
    print name


errmsg = 'Error!'
#create username
lbl_username = tk.Label(root, text="Username", bg="#a1dbcd")
ent_username = tk.Entry(root)

#pack username
lbl_username.pack(side= LEFT, fill=X)
ent_username.pack(side= LEFT, fill=X)

#basic enter for password
lbl_password = tk.Label(root, text="Password", bg="#a1dbcd")
ent_password = tk.Entry(root, show="*")

#pack password
lbl_password.pack(side= LEFT,fill=X)
ent_password.pack(side= LEFT,fill=X)
# btn = Tkinter.Button(window, text="Sign up", command=question)
Button(text='Set it up', command=setupDatabase).pack(padx=40, pady=10, side=LEFT)
Button(text='Unlock Directory', command=chooseDir).pack(padx=10, pady=20, side=RIGHT)
Button(text='Lock Directory', command=chooseDir).pack(padx=20, pady=20, side=RIGHT)

root.mainloop()


