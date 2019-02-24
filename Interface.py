# -*- coding: utf-8 -*-
import Tkinter as tk
import tkFileDialog
import tkMessageBox
import sys



def openFile(string, types=[('pdf files', '.pdf')]):
    #pour cacher l'autre root
    #root = Tkinter.Tk()
    #root.withdraw()

    filepath = tkFileDialog.askopenfilename(title=string,filetypes=types)
    return(filepath)


def openCorrige():
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

def openCopies():
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
        
        
    
def openEleves():
    global fileEleves
    temp = openFile('Liste des élèves', [('text files', '.txt')])
    if temp != "":
        fileEleves=temp
    strEleves.set(fileEleves.split('/')[-1])
    root.update_idletasks()
    
    

def validate():
    if fileCorrige != "" and fileCopies != "":
        root.destroy()




def on_closing(root):
    if tkMessageBox.askokcancel("Quitter", "Voulez-vous quitter ?"):
        root.destroy()
        sys.exit(0)



root = tk.Tk()
#root.configure(background='white')
root.title('Choix des pdf')
root.minsize(300,10)
root.iconbitmap("dev\logo.ico")


imageEx = tk.PhotoImage(file = 'Dev/IMTLD_RVB_Baseline.gif')
panelA = tk.Label(image=imageEx)
panelA.image = imageEx
panelA.grid(row=1, column=1)
labelTitle = tk.Label(root, width=52, height=5, font=("Arial Bold", 13), text="Correction automatique de grilles de TOEIC", takefocus=0, justify=tk.LEFT, bg="#FFFFFF")
labelTitle.grid(row=1, column=2)
#labelTitle.pack(side="top", fill="both", expand="yes", padx="10", pady="10")
    

fileCorrige = ""
strCorrige = tk.StringVar()
strCorrige.set('Aucun')

fileCopies = ""
strCopies= tk.StringVar()
strCopies.set('Aucun')

fileEleves = "noms.txt"
strEleves= tk.StringVar()
strEleves.set('Aucun')

progress = tk.StringVar()
progress.set('0%')


tk.Button(root, text ='Pdf du corrigé', width=20, height=1, command=openCorrige).grid(row=2, column=1, padx=5, pady=5)
l1 = tk.Label(root, textvariable =strCorrige)
l1.grid(row=2, column=2, sticky='W', padx=10)
tk.Button(root, text ='Pdf des copies', width=20, height=1, command=openCopies).grid(row=3, column=1, padx=5, pady=5)
l2 = tk.Label(root, textvariable =strCopies)
l2.grid(row=3, column=2, sticky='W', padx=10)
tk.Button(root, text ='Liste des élèves (optionnel)', width=20, height=1, command=openEleves).grid(row=4, column=1, padx=5, pady=5)
l3 = tk.Label(root, textvariable =strEleves)
l3.grid(row=4, column=2, sticky='W', padx=10)


buttonValidate = tk.Button(root, text ='Valider', width=20, height=1, command=validate)
buttonValidate.grid(row=5, column=1, columnspan=3, padx=5, pady=5)
buttonValidate.config(state=tk.DISABLED) 


def interface1():
    root.protocol("WM_DELETE_WINDOW", lambda:on_closing(root))
    root.mainloop()
    return(fileCorrige,fileCopies, fileEleves)




if __name__ == '__main__':
    a=interface1()
    print(a)
