# -*- coding: utf-8 -*-
from Interface import interface1
import export
from name import promptNames
from loading import loading
import tkMessageBox
import Tkinter as tk

import os
import shutil



def rename_images(names):
    path = "..\Results"
    try:
        shutil.rmtree(path)
    except:
        "aucun dossier results"
    if not os.path.exists(path):
        os.makedirs(path)
        os.makedirs(path+"\copies_corrigees")
    for i in range(len(names)):
        if len(names[i])>0:
            old_file = os.path.join("run", 'out'+ str(i) +'.jpg')
            new_file = os.path.join("..\Results\copies_corrigees", str(names[i])+'.jpg')
            shutil.copy2(old_file,new_file)
        else :
            shutil.copy2('run/out'+ str(i) +'.jpg', "..\Results\copies_corrigees")
        
    old_file = 'moyennes_classe.csv'
    new_file = os.path.join("../Results", 'moyennes_classe.csv')
    shutil.copy2(old_file,new_file)
    old_file = 'scores_individuels.csv'
    new_file = os.path.join("../Results", 'scores_individuels.csv')
    shutil.copy2(old_file,new_file)
    


def main():
    # get the names of the pdf files
    filepathCorr,filepathEleves, listeEleves = interface1();

    # get the scores while displaying loading bar
    answersCorr,answersEleves,scores = loading(filepathCorr,filepathEleves)
    
    # prompt the names of the students
    names = promptNames(scores[0], listeEleves)
    
    # export results
    export.exportIndiv(scores[0], names)
    export.exportClasse(scores[1],scores[2])
    
    # debug
    export.exportAnswersEleves(answersEleves, names)
    
    rename_images(names)
    
    root = tk.Tk()
    root.withdraw()
    tkMessageBox.showinfo("Terminé", "Export terminé : résultats dans moyennes_classe.csv et scores_individuels.csv")

    

"""
import cProfile

pr = cProfile.Profile()
pr.enable()
"""
main()
"""
pr.disable()

pr.print_stats(sort='cumtime')
"""
