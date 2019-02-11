from Tkinter import *
from PIL import Image
from PIL import ImageTk
from time import sleep
import tkFileDialog

fenetre = Tk()

fileCorrige = StringVar()
fileCopies = StringVar()
progress = StringVar()
fileCorrige.set('None')
fileCopies.set('None')
progress.set('0%')


def openFile(string):
    #pour cacher l'autre fenetre
    #root = Tkinter.Tk()
    #root.withdraw()

    filepath = tkFileDialog.askopenfilename(title=string,filetypes=[('pdf files', '.pdf')])
    return(filepath)


def openCorrige():
    fileCorrige.set(openFile('pdf du corrige'))
    fenetre.update_idletasks()

def openCopies():
    fileCopies.set(openFile('pdf des copies'))
    fenetre.update_idletasks()

def run():
    if fileCorrige.get() != 'None' and fileCopies.get() != 'None':
        fenetre.quit()


Button(fenetre, text ='pdf du corrige', command=openCorrige).grid(row=1, column=1)
l1 = Label(fenetre, textvariable =fileCorrige)
l1.grid(row=1, column=2)
Button(fenetre, text ='pdf des copies', command=openCopies).grid(row=2, column=1)
l2 = Label(fenetre, textvariable =fileCopies)
l2.grid(row=1, column=2)
Button(fenetre, text ='run', command=run).grid(row=3, column=1)
l3 = Label(fenetre, textvariable =progress)
l3.grid(row=3, column=2)

def interface1():
    fenetre.mainloop()
    return(fileCorrige.get(),fileCopies.get())

def interface2():
    fenetre.mainloop()
    return(fileCorrige.get(),fileCopies.get())


if __name__ == '__main__':
    a=interface("test")
    print(a)
