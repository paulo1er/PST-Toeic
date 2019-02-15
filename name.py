# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:48:13 2019

@author: Guillaume
"""

import Tkinter as tk
import tkMessageBox
from PIL import Image
from PIL import ImageTk
import cv2
import sys


 
def select_image(im):

    # grab a reference to the image panels
    global panelA
    # OpenCV represents images in BGR order; however PIL represents
    # images in RGB order, so we need to swap the channels
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    # convert the images to PIL format...
    im = Image.fromarray(im)
     
    # ...and then to ImageTk format
    im = ImageTk.PhotoImage(im)
       
        
    # if the panels are None, initialize them
    if panelA is None:
        # the first panel will store our original image
        panelA = tk.Label(image=im)
        panelA.image = im
        panelA.pack( padx=10, pady=10)
 
    # otherwise, update the image panels
    else:
        # update the pannels
        panelA.configure(image=im)
        panelA.image = im










def resize_name(n):
    images=[]
    for i in range(n):
        path="run/temp/out"+str(i)+".jpg"
        if len(path) > 0:
            # load the image from disk, resize it
            image = cv2.imread(path)
            
            width, height = image.shape[:2]
            y=int(0.022*height)
            h=int(0.05*height)
            x=int(0.02*width)
            w=int(0.66*width)
            last_name = image[y:y+h, x:x+w]
            last_name = cv2.copyMakeBorder(last_name,0,h,0,0,cv2.BORDER_CONSTANT,value=[0,0,0])
            
            x=int(0.73*width)
            first_name = image[y:y+h, x:x+w]
            names=last_name
            names[h:2*h, :] = first_name
            
            target_width = 500
            target_height = 160
            names = cv2.resize(names, (target_width, target_height))
            
            #cv2.imshow("names", names)
            #cv2.waitKey(0)
            images.append(names)
    return images




class ImageCatalogue:
    def changeName(self,valueName):
        self.names[self.i]=(valueName)
        
    def update(self):
        self.im = self.images[self.i]
        self.name = self.names[self.i]
        #print(self.names)
        
    def __init__(self, images):
        self.images = images
        self.n = len(images)
        self.names = [ "" for k in range(self.n) ]
        self.i = 0
        self.update()
      
    def next(self):
        if self.i < self.n -1:
            self.i+=1
        self.update()
        select_image(self.im)
    
    def prev(self):
        if self.i > 0 :
            self.i-=1
        self.update()
        select_image(self.im)
        

def prevImage(cat,valueName, strNumber):
    cat.changeName(valueName.get())
    cat.prev()
    valueName.set(cat.name)
    strNumber.set(str(cat.i+1) + " / "+str(cat.n))
    
    
def nextImage(cat,valueName, strNumber):
    cat.changeName(valueName.get())
    cat.next()  
    valueName.set(cat.name)
    strNumber.set(str(cat.i+1) + " / "+str(cat.n))


def validate(cat, root, valueName):
    cat.changeName(valueName.get())
    dupl=findDuplicates(cat.names)
    if "" in cat.names :
        message="Il manque un nom en position "+ str(1 + cat.names.index("")) +", continuer quand-même ?"
        if tkMessageBox.askokcancel("Valider", message):
            root.destroy()
    elif dupl:
        message="Le nom "+ str(dupl) +" est en double, continuer quand-même ?"
        if tkMessageBox.askokcancel("Valider", message):
            root.destroy()
    else:
        root.destroy()


def findDuplicates(in_list):  
    unique = set(in_list)  
    for each in unique:  
        count = in_list.count(each)  
        if count > 1:  
            return each  
    return False




def init(cat):
    # initialize the window toolkit along with the image panel
    root = tk.Tk()
    root.title('Saisie des noms')
    global panelA
    panelA = None
    
    
    select_image(cat.im)
    
    
    
    #Bouton valider
    btnFinish = tk.Button(root, text="Valider", command= lambda:validate(cat, root, valueName ))
    btnFinish.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
    
    
    
    # Images suivantes et precedentes
    Frame3 = tk.Frame(root, borderwidth=2, relief=tk.GROOVE)
    Frame3.pack(side=tk.BOTTOM, padx=10, pady=10)
    btn0 = tk.Button(Frame3, text="Précédent", command= lambda:prevImage(cat,valueName, strNumber))
    btn0.pack(side="left", fill="both", expand="yes", padx="10", pady="10")
    
    btn = tk.Button(Frame3, text="Suivant", command= lambda:nextImage(cat,valueName, strNumber))
    btn.pack(side="right", fill="both", expand="yes", padx="10", pady="10")
    

    
    # Nom et prénom
    Frame1 = tk.Frame(root, borderwidth=2, relief=tk.GROOVE)
    Frame1.pack( padx=30, pady=30)
    labelName = tk.Label(Frame1, text="Nom, prénom")
    labelName.pack()
    # entrée
    valueName = tk.StringVar() 
    entree = tk.Entry(Frame1, textvariable=valueName, width=60)
    entree.pack()
    
    
    strNumber = tk.StringVar() 
    strNumber.set("1 / "+ str(cat.n))
    labelNumber = tk.Label(Frame1, textvariable =strNumber)
    labelNumber.pack()
    

    return root
    



def on_closing(root):
    if tkMessageBox.askokcancel("Quitter", "Voulez-vous quitter ?"):
        root.destroy()
        sys.exit(0)
        



# main
def promptNames(n):    
    images = resize_name(n)
    cat = ImageCatalogue(images)
    root = init(cat)
    root.protocol("WM_DELETE_WINDOW", lambda:on_closing(root))
    root.mainloop()
    #print(cat.names)
    return cat.names



if __name__ == '__main__':
    """import cProfile
     
    pr = cProfile.Profile()
    pr.enable()
    """
    promptNames(7)
    """
    pr.disable()
     
    pr.print_stats(sort='cumtime')
    """

