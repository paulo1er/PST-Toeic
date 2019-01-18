

def export(results):
    f = open("export.csv", "w")
    csv = "name;listening;reading;total"
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
