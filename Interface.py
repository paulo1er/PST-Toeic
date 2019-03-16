# -*- coding: utf-8 -*-


"""
This file contains functions to display the UI for choosing the input files
"""


import Tkinter as tk
import tkFileDialog
import tkMessageBox
import sys


fileCorrige = ""
fileCopies = ""
fileEleves = ""


# dialog window to open a file
def openFile(string, types=[('pdf files', '.pdf')]):
    filepath = tkFileDialog.askopenfilename(title=string,filetypes=types)
    return(filepath)

# opens a dialog window to open a pdf file and saves the result in fileCorrige
def openCorrige(root, strCorrige, buttonValidate):
    global fileCorrige
    temp = openFile('Pdf du corrigé')
    if temp != "":
        fileCorrige=temp
    strCorrige.set(fileCorrige.split('/')[-1])
    root.update_idletasks()
    if fileCorrige != "" and fileCopies != "":
        buttonValidate.config(state=tk.NORMAL)
    else:
        buttonValidate.config(state=tk.DISABLED)

# opens a dialog window to open a pdf file and saves the result in fileCopies
def openCopies(root, strCopies, buttonValidate):
    global fileCopies
    temp = openFile('Pdf des copies')
    if temp != "":
        fileCopies=temp
    strCopies.set(fileCopies.split('/')[-1])
    root.update_idletasks()
    if fileCorrige != "" and fileCopies != "":
        buttonValidate.config(state=tk.NORMAL)
    else:
        buttonValidate.config(state=tk.DISABLED)
        
        
# opens a dialog window to open a txt file and saves the result in fileEleves 
def openEleves(root, strEleves):
    global fileEleves
    temp = openFile('Liste des élèves', [('text files', '.txt')])
    if temp != "":
        fileEleves=temp
    strEleves.set(fileEleves.split('/')[-1])
    root.update_idletasks()
    
    
# start the program
def validate(root):
    if fileCorrige != "" and fileCopies != "":
        root.destroy()



# displays warning if the user wants to close window
def on_closing(root):
    if tkMessageBox.askokcancel("Quitter", "Voulez-vous quitter ?"):
        root.destroy()
        sys.exit(0)


# main function : displays the UI for choosing the input files
def interface():
    root = tk.Tk()
    root.title('Choix des pdf')
    root.minsize(300,10)
    root.iconbitmap("dev\logo.ico")
    
    # IMT logo
    imageEx = tk.PhotoImage(file = 'Dev/IMTLD_RVB_Baseline.gif')
    panelA = tk.Label(image=imageEx)
    panelA.image = imageEx
    panelA.grid(row=1, column=1)
    labelTitle = tk.Label(root, width=52, height=5, font=("Arial Bold", 13), text="Correction automatique de grilles de TOEIC", takefocus=0, justify=tk.LEFT, bg="#FFFFFF")
    labelTitle.grid(row=1, column=2)
 
    
    strCorrige = tk.StringVar()
    strCorrige.set('Aucun')
    

    strCopies= tk.StringVar()
    strCopies.set('Aucun')
    

    strEleves= tk.StringVar()
    strEleves.set('Aucun')
    
    
    tk.Button(root, text ='Pdf du corrigé', width=20, height=1, command=lambda:openCorrige(root, strCorrige, buttonValidate)).grid(row=2, column=1, padx=5, pady=5)
    l1 = tk.Label(root, textvariable =strCorrige)
    l1.grid(row=2, column=2, sticky='W', padx=10)
    tk.Button(root, text ='Pdf des copies', width=20, height=1, command=lambda:openCopies(root, strCopies, buttonValidate)).grid(row=3, column=1, padx=5, pady=5)
    l2 = tk.Label(root, textvariable =strCopies)
    l2.grid(row=3, column=2, sticky='W', padx=10)
    tk.Button(root, text ='Liste des élèves (optionnel)', width=20, height=1, command=lambda:openEleves(root, strEleves)).grid(row=4, column=1, padx=5, pady=5)
    l3 = tk.Label(root, textvariable =strEleves)
    l3.grid(row=4, column=2, sticky='W', padx=10)
    
    
    buttonValidate = tk.Button(root, text ='Valider', width=20, height=1, command=lambda:validate(root))
    buttonValidate.grid(row=5, column=1, columnspan=3, padx=5, pady=5)
    buttonValidate.config(state=tk.DISABLED) 


    # displays warning if the user wants to close window
    root.protocol("WM_DELETE_WINDOW", lambda:on_closing(root))
    root.mainloop()
    return(fileCorrige,fileCopies, fileEleves)



# for testing only
if __name__ == '__main__':
    a=interface()
    print(a)
