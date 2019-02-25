# -*- coding: utf-8 -*-
from Interface import interface1
import export
from name import promptNames
from loading import loading
import tkMessageBox



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
