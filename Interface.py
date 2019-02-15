import Tkinter as tk
import tkFileDialog
import tkMessageBox
import sys



def openFile(string):
    #pour cacher l'autre fenetre
    #root = Tkinter.Tk()
    #root.withdraw()

    filepath = tkFileDialog.askopenfilename(title=string,filetypes=[('pdf files', '.pdf')])
    return(filepath)


def openCorrige():
    global fileCorrige
    temp = openFile('pdf du corrige')
    if temp != "":
        fileCorrige=temp
    strCorrige.set(fileCorrige.split('/')[-1])
    fenetre.update_idletasks()
    

def openCopies():
    global fileCopies
    temp = openFile('pdf des copies')
    if temp != "":
        fileCopies=temp
    strCopies.set(fileCopies.split('/')[-1])
    fenetre.update_idletasks()
    
    
    

def validate():
    if fileCorrige != "" and fileCopies != "":
        fenetre.destroy()




def on_closing(root):
    if tkMessageBox.askokcancel("Quitter", "Voulez-vous quitter ?"):
        root.destroy()
        sys.exit(0)



fenetre = tk.Tk()
fenetre.title('Choix des pdf')
fenetre.minsize(300,10)




fileCorrige = ""
strCorrige = tk.StringVar()
strCorrige.set('Aucun')

fileCopies = ""
strCopies= tk.StringVar()
strCopies.set('Aucun')

progress = tk.StringVar()
progress.set('0%')


tk.Button(fenetre, text ='pdf du corrige', command=openCorrige).grid(row=1, column=1)
l1 = tk.Label(fenetre, textvariable =strCorrige)
l1.grid(row=1, column=2)
tk.Button(fenetre, text ='pdf des copies', command=openCopies).grid(row=2, column=1)
l2 = tk.Label(fenetre, textvariable =strCopies)
l2.grid(row=2, column=2)


tk.Button(fenetre, text ='Valider', command=validate).grid(row=3, column=1)
l3 = tk.Label(fenetre, textvariable =progress)
l3.grid(row=3, column=2)



def interface1():
    fenetre.protocol("WM_DELETE_WINDOW", lambda:on_closing(fenetre))
    fenetre.mainloop()
    return(fileCorrige,fileCopies)




if __name__ == '__main__':
    a=interface1()
    print(a)
