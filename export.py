

def export(results):
    f = open("export.csv", "w")
    csv = "name;total;listening;reading;Description d'images;Question-Response;Dialogues;Discussions - Annonces;Phrases a completer;Textes a completer;Lecture contenus rediriges,  Passages simples;Lecture contenus rediriges, Passages multiples"
    csv += "\n"

    ic=1
    for result in results:
        csv += "etudiant " + str(ic) + ";"
        for i in result:
            csv += str(i) + ";"
        csv += "\n"
        ic += 1
    print >>f, csv
    print("Fichier exporte dans export.csv")
    f.close()
