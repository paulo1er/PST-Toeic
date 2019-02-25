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
from tkinter_autocomplete import AutocompleteEntry
import os
 
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
        panelA.pack()
 
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
        
    def __init__(self, images, scores):
        self.scores = scores
        self.images = images
        self.n = len(images)
        self.names = [ "" for k in range(self.n) ]
        self.i = 0
        self.btnPrec = None
        self.btnSuiv = None
        self.update()
      
    def next(self):
        if self.i < self.n -2:
            self.btnPrec.config(state=tk.NORMAL)
        else:
            self.btnSuiv.config(state=tk.DISABLED)
        if self.i < self.n -1:
            self.i+=1
        self.update()
        select_image(self.im)
    
    def prev(self):
        if self.i > 1 :
            self.btnSuiv.config(state=tk.NORMAL)
        else:
            self.btnPrec.config(state=tk.DISABLED)     
        if self.i > 0 :
            self.i-=1
        self.update()
        select_image(self.im)
        
    def getScore(self):
        return self.scores[self.i][0]
        

def prevImage(cat,valueName, strNumber, strScore, entree, isAutocomplete):
    cat.changeName(valueName.get())
    cat.prev()
    valueName.set(cat.name)
    strNumber.set(str(cat.i+1) + " / "+str(cat.n))
    strScore.set("Score : " + str(cat.getScore()))
    if isAutocomplete:
        entree._update_autocomplete(None)
        entree.entry.focus()
    else:
        entree.focus()
    
    
    
def nextImage(cat,valueName, strNumber, strScore, entree, isAutocomplete):
    cat.changeName(valueName.get())
    cat.next()  
    valueName.set(cat.name)
    strNumber.set(str(cat.i+1) + " / "+str(cat.n))
    strScore.set("Score : " + str(cat.getScore()))
    if isAutocomplete:
        entree._update_autocomplete(None)
        entree.entry.focus()
    else:
        entree.focus()


def validate(cat, root, valueName):
    cat.changeName(valueName.get())
    dupl=findDuplicates(cat.names)
    if "" in cat.names :
        message="Il manque un nom en position "+ str(1 + cat.names.index("")) +", continuer quand même ?"
        if tkMessageBox.askokcancel("Valider", message):
            root.destroy()
    elif dupl:
        message="Le nom "+ str(dupl) +" est en double, continuer quand même ?"
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




def init(cat, fileEleves="noms.txt"):
    # initialize the window toolkit along with the image panel
    root = tk.Tk()
    root.title('Saisie des noms')
    root.iconbitmap("dev\logo.ico")
    global panelA
    panelA = None
    
    
    select_image(cat.im)
    
    # Nom et prénom
    Frame1 = tk.Frame(root, borderwidth=0, relief=tk.GROOVE)
    labelName = tk.Label(Frame1, text="Nom Prénom")
    labelName.pack(pady="5")
    
    # Entrée du nom
    isAutocomplete = False
    if os.path.exists(fileEleves):
       with open(fileEleves, 'rb') as entriesFile:
           try:
               # entrée avec autocomplete
               entries = entriesFile.read().split('\n')
               entries.sort()
               
               frameEntree = tk.Frame(Frame1)
               frameEntree.pack()   
               entree = AutocompleteEntry(frameEntree)
               valueName = entree.text
               entree.build(entries, no_results_message=None, max_entries=5)
               isAutocomplete = True
           except : 
               print "erreur de l'importation du fichier noms.txt" 
    # entrée sans autocomplete
    if not isAutocomplete:
       valueName = tk.StringVar() 
       entree = tk.Entry(Frame1, textvariable=valueName, width=60)


    # Images precedentes, compteur et suivantes
    frame3 = tk.Frame(root, relief=tk.GROOVE)
    frame3.pack(side=tk.TOP, padx=10, pady=10)
    btnPrec = tk.Button(frame3, text="Précédent", width=20, height=1, command=lambda:prevImage(cat,valueName, strNumber, strScore, entree, isAutocomplete))
    btnPrec.grid(row=1, column=1, padx=10)
    btnPrec.config(state=tk.DISABLED)
    
    strNumber = tk.StringVar() 
    strNumber.set("1 / "+ str(cat.n))
    labelNumber = tk.Label(frame3, textvariable =strNumber)
    labelNumber.grid(row=1, column=2, padx=5, pady=6)
    
    btnSuiv = tk.Button(frame3, text="Suivant", width=20, height=1, command=lambda:nextImage(cat,valueName, strNumber, strScore, entree, isAutocomplete))
    btnSuiv.grid(row=1, column=3, padx=10)
    
    cat.btnSuiv = btnSuiv
    cat.btnPrec = btnPrec
    
    #Affichage du score
    strScore = tk.StringVar() 
    strScore.set("Score : " + str(cat.getScore()))
    labelScore = tk.Label(root, textvariable =strScore)
    labelScore.pack( padx="10", pady="8")
    
    #Bouton valider
    btnFinish = tk.Button(root, text="Valider", width=30, height=1, command= lambda:validate(cat, root, valueName ))
    btnFinish.pack(side="bottom",  padx="10", pady="18")
    
    # affichage du Nom et prénom et entrée du nom
    Frame1.pack( padx=30, pady=5)
    entree.pack(pady="3") 
    
    return root
    



def on_closing(root):
    if tkMessageBox.askokcancel("Quitter", "Voulez-vous quitter ?"):
        root.destroy()
        sys.exit("closed window")
        



# main
def promptNames(scores, fileEleves):    
    n=len(scores)
    images = resize_name(n)
    cat = ImageCatalogue(images, scores)
    root = init(cat, fileEleves)
    root.protocol("WM_DELETE_WINDOW", lambda:on_closing(root))
    root.mainloop()
    print "names :" , cat.names
    return cat.names



if __name__ == '__main__':
    """import cProfile
     
    pr = cProfile.Profile()
    pr.enable()
    """
    promptNames([[310, 190, 120, '="4 / 6"', '="7 / 25"', '="20 / 39"', '="13 / 30"', '="10 / 30"', '="5 / 16"', '="17 / 29"', '="8 / 25"'], [780, 150, 130, '="3 / 6"', '="8 / 25"', '="19 / 39"', '="9 / 30"', '="14 / 30"', '="4 / 16"', '="18 / 29"', '="6 / 25"'], [330, 205, 125, '="3 / 6"', '="3 / 25"', '="25 / 39"', '="15 / 30"', '="10 / 30"', '="2 / 16"', '="18 / 29"', '="11 / 25"'], [255, 170, 85, '="2 / 6"', '="8 / 25"', '="19 / 39"', '="12 / 30"', '="5 / 30"', '="4 / 16"', '="17 / 29"', '="9 / 25"'], [275, 170, 105, '="0 / 6"', '="7 / 25"', '="20 / 39"', '="14 / 30"', '="9 / 30"', '="6 / 16"', '="13 / 29"', '="10 / 25"'], [345, 225, 120, '="3 / 6"', '="7 / 25"', '="24 / 39"', '="15 / 30"', '="9 / 30"', '="4 / 16"', '="20 / 29"', '="7 / 25"'], [845, 440, 405, '="1 / 6"', '="20 / 25"', '="35 / 39"', '="27 / 30"', '="29 / 30"', '="15 / 16"', '="22 / 29"', '="20 / 25"']], "noms.txt")
    """
    pr.disable()
     
    pr.print_stats(sort='cumtime')
    """

