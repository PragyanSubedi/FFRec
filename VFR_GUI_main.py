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
from tkFileDialog import askopenfilename


url='http://192.168.0.109:8080/shot.jpg'

#Set up GUI

root = tk.Tk()
root.geometry("1260x640+80+50")
root.resizable(width=False, height=False)

#Makes main window

root.wm_title("Floating Faces")
root.config(background="#d9d9d9")

def quit_app():
    root.quit()

def setupDatabase():
    print("asd")
    import VFR_GUI_DC


def chooseDir():
    name = askopenfilename()
    print name

style = ttk.Style()
ttk.Style().theme_use('alt')

# Inserting background image

# photos = PhotoImage(file="images/b5.png",width=1260)
# label= Label(root,image=photos)
# label.grid(row=0,column=50, rowspan= 200,columnspan=100)

#Insering logo image

photo = PhotoImage(file="images/logo.png")
label= Label(root,image=photo)
label.grid(row=2,column=50, padx=90,pady=50,rowspan= 10)

#FLOATING FACES text

theLabel= tk.Label(root, text="FLOATING FACES",
                   foreground="black",
                   font="Helvetica 20 bold ").grid(row=2, column=80, ipady=100, sticky=N)

# Button to call Dataset creator GUI


theButton = tk.Button(text='Set it up',
                      command=setupDatabase,
                      activebackground='white',
                      foreground="ivory2",
                      background="gray23",
                      font="Helvetica 14 bold italic",
                      borderwidth=7)
theButton.grid(row=3, column=60)

# Opens directory listing

theButton = tk.Button(text='Lock app',
                      command=chooseDir,
                      activebackground='white',
                      foreground="ivory2",
                      background="gray23",
                      font="Helvetica 14 bold italic",
                      borderwidth=7)
theButton.grid(row=3, column=80 )

# Opens directory listing

theButton = tk.Button(text='Unlock app',
                      command=chooseDir,
                      activebackground='white',
                      foreground="ivory2",
                      background="gray23",
                      font="Helvetica 14 bold italic",
                      borderwidth=7)
theButton.grid(row=3, column=100 )

# COPYRIGHT Label

theLabel= tk.Label(root, text="(c) 2017 FLOATING FACES ALL RIGHTS RESERVED.",
                   foreground="black",
                   font="Helvetica 8 italic").grid(row=6, column=80)

# EXIT Button

theButton = tk.Button(text='Exit',
                      command=quit_app,
                      activebackground='white',
                      foreground="ivory2",
                      background="gray23",
                      font="Helvetica 14 bold italic",
                      borderwidth=7)
theButton.grid(row=11, column=100, sticky=S, ipadx=36)

#Starts GUI

root.mainloop()


