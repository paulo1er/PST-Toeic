# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:33:59 2019

@author: Guillaume
"""

import Tkinter as tk
from Queue import Queue
import ttk, threading
import tkMessageBox
import os

#imports personnels
from solve import getAnswers
from score import compareAll


# Function to check state of thread 
def progress(thread, queue, parent):
    thread.start()
    progressBar = ttk.Progressbar(parent,length=250, orient='horizontal', mode='indeterminate')
    progressBar.pack()
    progressBar.start()

    # checks whether thread is alive 
    while thread.is_alive():
        parent.update()
        pass

    # once thread is no longer active, destroy the GUI
    parent.destroy()
   
    # retrieves object from queue 
    work = queue.get()
    return work




def on_closing(root):
    tkMessageBox.showinfo("Interruption", "Veuillez ne pas quitter pendant cette étape, qui dure environ 2min pour 100 copies")
    
        


# threaded work
def threadedWork(filepathCorr,filepathEleves, queue):
    pdfinfo_path = os.getcwd() + '\\poppler-0.68.0\\bin' 
    os.environ['PATH'] = pdfinfo_path + ';' + os.environ['PATH']
    answersCorr=getAnswers(filepathCorr)[0]
    answersEleves=getAnswers(filepathEleves)
    
    scores=compareAll(answersCorr,answersEleves)
    ret =  answersCorr,answersEleves, scores    
    queue.put(ret)





def loading(filepathCorr,filepathEleves):    
    queue = Queue()
    root = tk.Tk()
    root.iconbitmap("dev\logo.ico")
    root.title('Chargement')
    root.protocol("WM_DELETE_WINDOW", lambda:on_closing(root))

    thread1 = threading.Thread(target=threadedWork, args=(filepathCorr,filepathEleves, queue))
    
    work = progress(thread1, queue, root)
   
    root.mainloop()
    return work




if __name__ == '__main__':
    filepathCorr = "Scan test/Toeic Correction.pdf"
    filepathEleves = "Scan test/Toeic Test 1.pdf"
    
    #import cProfile
    #pr = cProfile.Profile()
    #pr.enable()
    
    loading(filepathCorr,filepathEleves)
    
    #pr.disable()
    #pr.print_stats(sort='cumtime')
    
