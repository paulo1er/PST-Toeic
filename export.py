# -*- coding: utf-8 -*-

def exportIndiv(results, names):
    f = open("scores_individuels.csv", "w")
    csv = "Nom;Total;Listening;Reading;Description d'images;Question-Response;Dialogues;Discussions - Annonces;Phrases a completer;Textes a completer;Lecture contenus rediriges,  Passages simples;Lecture contenus rediriges, Passages multiples"
    csv += "\n"

    ic=1
    for result in results:
        csv += names[ic-1] + ";"
        for i in result:
            csv += str(i) + ";"
        csv += "\n"
        ic += 1
    csv = csv.encode('utf-8');
    print >>f, csv
    print("Fichier exporte dans scores_individuels.csv")
    f.close()



def questionsEntre(a,b, percentages):
    temp=""
    res=""
    res+=";"
    for i in range(a,b):
        res +='Question '+ str(i+1) + ";"
        temp += str(percentages[i]) +  "%;"
    res += "\n"
    res+=";"
    res += temp
    return res



def exportClasse(exercisesRes, percentages):
    f = open("moyennes_classe.csv", "w")
    csv = "Score moyen"
    csv += "\n"
    csv += str(exercisesRes[0])
    csv += "\n\n\n"


    csv += "moyenne listening"
    csv += "\n"
    csv += str(exercisesRes[1])
    csv += "\n\n"


    csv += "Description d'images"
    csv += "\n"
    csv += str(exercisesRes[3])
    csv += "\n"

    csv += questionsEntre(0,6, percentages)
    csv += "\n\n"


    csv += "Question-Response"
    csv += "\n"
    csv += str(exercisesRes[4])
    csv += "\n"

    csv += questionsEntre(6,31, percentages)
    csv += "\n\n"


    csv += "Dialogues"
    csv += "\n"
    csv += str(exercisesRes[5])
    csv += "\n"

    csv += questionsEntre(31,70, percentages)
    csv += "\n\n"


    csv += "Discussions - Annonces"
    csv += "\n"
    csv += str(exercisesRes[6])
    csv += "\n"

    csv += questionsEntre(70,100, percentages)
    csv += "\n\n"


    csv += "\n\n"




    csv += "moyenne reading"
    csv += "\n"
    csv += str(exercisesRes[2])
    csv += "\n\n"


    csv += "Phrases a completer"
    csv += "\n"
    csv += str(exercisesRes[7])
    csv += "\n"

    csv += questionsEntre(100,130, percentages)
    csv += "\n\n"


    csv += "Textes a completer"
    csv += "\n"
    csv += str(exercisesRes[8])
    csv += "\n"

    csv += questionsEntre(130,146, percentages)
    csv += "\n\n"



    csv += "Lecture contenus rediriges,  Passages simples"
    csv += "\n"
    csv += str(exercisesRes[9])
    csv += "\n"

    csv += questionsEntre(146,175, percentages)
    csv += "\n\n"


    csv += "Lecture contenus rediriges,  Passages multiples"
    csv += "\n"
    csv += str(exercisesRes[10])
    csv += "\n"

    csv += questionsEntre(175,200, percentages)
    csv += "\n\n"


    csv = csv.encode('utf-8');
    print >>f, csv
    print("Fichier exporte dans moyennes_classe.csv")
    f.close()


def exportAnswersEleves(answersEleves, names):
    f = open("reponses_eleves.csv", "w")
    csv = " ;"
    for i in range(1, 201, 1) :
        csv += str(i) + ";"
    csv += "\n"

    ic=1
    for answersEleve in answersEleves:
        csv += names[ic-1] + ";"
        for i in answersEleve:
            csv += str(i) + ";"
        csv += "\n"
        ic += 1
    csv = csv.encode('utf-8');
    print >>f, csv
    print("Fichier exporte dans reponses_eleves.csv")
    f.close()
