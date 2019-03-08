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
    path = "Résultats"
    try:
        shutil.rmtree(path)
    except:
        print "aucun dossier Résultats"
    if not os.path.exists(path):
        os.makedirs(path)
        os.makedirs(path+"\copies_corrigees")
    for i in range(len(names)):
        if len(names[i])>0:
            old_file = os.path.join("run", 'out'+ str(i) +'.jpg')
            name = str(names[i].encode('utf-8').strip())
            try:
                new_file = os.path.join(".\Résultats\copies_corrigees", name +'.jpg')
                shutil.copy2(old_file,new_file)
            except : 
                #si il reste encore des caracteres speciaux
                shutil.copy2('run/out'+ str(i) +'.jpg', ".\Résultats\copies_corrigees")
        else :
            shutil.copy2('run/out'+ str(i) +'.jpg', ".\Résultats\copies_corrigees")
        
    old_file = 'moyennes_classe.csv'
    new_file = os.path.join("./Résultats", 'moyennes_classe.csv')
    shutil.move(old_file,new_file)
    old_file = 'scores_individuels.csv'
    new_file = os.path.join("./Résultats", 'scores_individuels.csv')
    shutil.move(old_file,new_file)
    


def main():
     
    path = "run"
    try:
        shutil.rmtree(path)
    except:
        print "aucun dossier run"
    if not os.path.exists(path):
        os.makedirs(path)
    
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
    # export.exportAnswersEleves(answersEleves, names)
    
    rename_images(names)
    
    root = tk.Tk()
    root.withdraw()
    tkMessageBox.showinfo("Terminé", "Export terminé : résultats dans moyennes_classe.csv et scores_individuels.csv")
    root.destroy()
    

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
