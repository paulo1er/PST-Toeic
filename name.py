# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 09:48:13 2019

@author: Guillaume
"""


"""
This file contains functions to display the UI for prompting the names of the students
"""


import Tkinter as tk
import tkMessageBox
from PIL import Image
from PIL import ImageTk
import cv2 as cv
import os
import sys

#imports personnels
from tkinter_autocomplete import AutocompleteEntry


# updates the image when the user navigates
def select_image(im):

    # grab a reference to the image panels
    global panelA
    # OpenCV represents images in BGR order; however PIL represents
    # images in RGB order, so we need to swap the channels
    im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
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


# before displaying the interface, crops ALL the images to display onl the names
# also prints the scores on each one
def resize_name(n, score):
    images=[]
    for i in range(n):
        path="run/out"+str(i)+".jpg"
        # for each student
        if len(path) > 0:
            image = cv.imread(path)
            
            # print the score onthe image and saves it           
            fontface = cv.FONT_HERSHEY_SIMPLEX
            fontscale = 3
            fontcolor = (255, 0, 0)
            thickness=3
            cv.putText(image, str(score[i][0]), (400, 250), fontface, fontscale, fontcolor, thickness) 
            cv.imwrite(path,image)
            
            # resize the 2 images
            width, height = image.shape[:2]
            y=int(0.022*height)
            h=int(0.05*height)
            x=int(0.02*width)
            w=int(0.66*width)
            last_name = image[y:y+h, x:x+w]
            last_name = cv.copyMakeBorder(last_name,0,h,0,0,cv.BORDER_CONSTANT,value=[0,0,0])
            
            x=int(0.73*width)
            first_name = image[y:y+h, x:x+w]
            names=last_name
            
            #merge the images
            names[h:2*h, :] = first_name
            
            # resize the image
            target_width = 500
            target_height = 160
            names = cv.resize(names, (target_width, target_height))
            
            images.append(names)
    return images



# object containing all the informations of the students and the images
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
        

# called upon pressing "previous" button
def prevImage(cat,valueName, strNumber, strScore, entree, isAutocomplete):
    cat.changeName(valueName.get())
    cat.prev()
    valueName.set(cat.name)
    # change the displayed index 
    strNumber.set(str(cat.i+1) + " / "+str(cat.n))
    strScore.set("Score : " + str(cat.getScore()))
    if isAutocomplete:
        entree._update_autocomplete(None)
        entree.entry.focus()
    else:
        entree.focus()
    
    
# called upon pressing "next" button   
def nextImage(cat,valueName, strNumber, strScore, entree, isAutocomplete):
    cat.changeName(valueName.get())
    cat.next()  
    valueName.set(cat.name)
    # change the displayed index 
    strNumber.set(str(cat.i+1) + " / "+str(cat.n))
    strScore.set("Score : " + str(cat.getScore()))
    if isAutocomplete:
        entree._update_autocomplete(None)
        entree.entry.focus()
    else:
        entree.focus()


# called upon pressing "validate" button at the end of prompt
def validate(cat, root, valueName):
    cat.changeName(valueName.get())

    # remove chars not suitable for windows file names
    illegal = ['NUL','\\','//',':','*','"','<','>','|','/','?',';',","]
    for name in cat.names:
        name.encode("utf-8")
        for i in illegal:
            name = name.replace(i, '')
            
    # cancels validation if there are duplicate names
    dupl=findDuplicates( filter(None, cat.names))
    if dupl: 
        message="Le nom "+ str(dupl) +" est en double, veuillez en changer un"
        tkMessageBox.showwarning("Doublon", message)
    
    # warns if there lacks some names
    elif "" in cat.names :
        message="Il manque un nom en position "+ str(1 + cat.names.index("")) +", continuer quand même ?"
        # if user bypasses warning : OK
        if tkMessageBox.askokcancel("Valider", message):
            root.destroy()
    # if everything correct
    else:
        root.destroy()


# true if there are dulicates in list
def findDuplicates(in_list):  
    unique = set(in_list)  
    for each in unique:  
        count = in_list.count(each)  
        if count > 1:  
            return each  
    return False



# initialize the UI
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


    # Image precedente
    frame3 = tk.Frame(root, relief=tk.GROOVE)
    frame3.pack(side=tk.TOP, padx=10, pady=10)
    btnPrec = tk.Button(frame3, text="Précédent", width=20, height=1, command=lambda:prevImage(cat,valueName, strNumber, strScore, entree, isAutocomplete))
    btnPrec.grid(row=1, column=1, padx=10)
    btnPrec.config(state=tk.DISABLED)
    
    # compteur d'images
    strNumber = tk.StringVar() 
    strNumber.set("1 / "+ str(cat.n))
    labelNumber = tk.Label(frame3, textvariable =strNumber)
    labelNumber.grid(row=1, column=2, padx=5, pady=6)
    
    # Image suivante
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
    


# displays warning if the user wants to close window
def on_closing(root):
    if tkMessageBox.askokcancel("Quitter", "Voulez-vous quitter ?"):
        root.destroy()
        sys.exit("closed window")
        



# main function : displays the UI for prompting the names of the students
# returns the prompted names
def promptNames(scores, fileEleves='noms.txt'):    
    n=len(scores)
    images = resize_name(n,scores)
    cat = ImageCatalogue(images, scores)
    root = init(cat, fileEleves)
    
    # displays warning if the user wants to close window
    root.protocol("WM_DELETE_WINDOW", lambda:on_closing(root))
    
    root.mainloop()
    return cat.names


# for testing only
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

