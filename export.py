

def exportIndiv(results, names):
    f = open("scores_individuels.csv", "w")
    csv = "name;total;listening;reading;Description d'images;Question-Response;Dialogues;Discussions - Annonces;Phrases a completer;Textes a completer;Lecture contenus rediriges,  Passages simples;Lecture contenus rediriges, Passages multiples"
    csv += "\n"

    ic=1
    for result in results:
        csv += names[ic-1][0]+" "+names[ic-1][1] + ";"
        for i in result:
            csv += str(i) + ";"
        csv += "\n"
        ic += 1
    print >>f, csv
    print("Fichier exporte dans scores_individuels.csv")
    f.close()


def exportClasse(exercisesRes, percentages):
    f = open("moyennes_classe.csv", "w")
    csv = "Score moyen;moyenne listening;moyenne reading;Description d'images;Question-Response;Dialogues;Discussions - Annonces;Phrases a completer;Textes a completer;Lecture contenus rediriges,  Passages simples;Lecture contenus rediriges, Passages multiples"
    csv += "\n"

    for i in exercisesRes:
        csv += str(i) + ";"
    csv += "\n"
    csv += "\n"
    csv += "\n"

    for i in range(len(percentages)):
        csv +='Question '+ str(i+1) + ";"
    csv += "\n"
    for i in percentages:
        csv += str(i) + "%;"
    print >>f, csv
    print("Fichier exporte dans moyennes_classe.csv")
    f.close()


def exportAnswersEleves(answersEleves, names):
    f = open("answersEleves.csv", "w")
    csv = " ;"
    for i in range(1, 201, 1) :
        csv += str(i) + ";"
    csv += "\n"

    ic=1
    for answersEleve in answersEleves:
        csv += names[ic-1][0]+" "+names[ic-1][1] + ";"
        for i in answersEleve:
            csv += str(i) + ";"
        csv += "\n"
        ic += 1
    print >>f, csv
    print("Fichier exporte dans answersEleves.csv")
    f.close()
