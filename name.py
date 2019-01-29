# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:48:13 2019

@author: Guillaume
"""


	
# import the necessary packages
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import tkFileDialog
import cv2

from resize import resize
 
def select_image():
    # grab a reference to the image panels
    global panelA, panelB
    path="Grille_Toeic-15-1.jpg"
    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk, convert it to grayscale, and detect
        # edges in it
        image = resize(cv2.imread(path))
        
        

        width, height = image.shape[:2]
        y=int(0.022*height)
        h=int(0.05*height)
        x=int(0.01*width)
        w=int(0.63*width)
        first_name = image[y:y+h, x:x+w]
        x=int(0.65*width)
        last_name = image[y:y+h, x:x+w]
        
        target_width = 500
        target_height = 80
        first_name = cv2.resize(first_name, (target_width, target_height))
        last_name = cv2.resize(last_name, (target_width, target_height))
        
        
        #cv2.imshow("cropped", last_name)
        #cv2.waitKey(0)
        


        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        first_name = cv2.cvtColor(first_name, cv2.COLOR_BGR2RGB)
        last_name = cv2.cvtColor(last_name, cv2.COLOR_BGR2RGB)
        # convert the images to PIL format...
        first_name = Image.fromarray(first_name)
        last_name = Image.fromarray(last_name)
         
        # ...and then to ImageTk format
        first_name = ImageTk.PhotoImage(first_name)
        last_name = ImageTk.PhotoImage(last_name)
       
        
    # if the panels are None, initialize them
    if panelA is None or panelB is None:
        # the first panel will store our original image
        panelA = Label(image=first_name)
        panelA.image = first_name
        panelA.pack( padx=10, pady=10)
         
        # while the second panel will store the edge map
        panelB = Label(image=last_name)
        panelB.image = last_name
        panelB.pack(padx=10, pady=10)
 
    # otherwise, update the image panels
    else:
        # update the pannels
        panelA.configure(image=first_name)
        panelB.configure(image=last_name)
        panelA.image = first_name
        panelB.image = last_name






# initialize the window toolkit along with the two image panels
root = Tk()
panelA = None
panelB = None
 
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI

select_image()
#btn = Button(root, text="Select an image", command=select_image)

#btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

l1 = Label(root, text="First Name")
#btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
l2 = Label(root, text="Last Name")
#btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
"""
e1 = Entry(l1)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
e2 = Entry(l1)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
"""


 
# kick off the GUI
root.mainloop()

