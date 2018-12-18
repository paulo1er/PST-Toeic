

def export(results):
    f = open("export.csv", "w")
    csv = " ,"
    for i in range(1, 201, 1) :
        csv += str(i) + ","
    csv += "\n"

    ic=1
    for result in results:
        csv += "etudiant " + str(ic) + ","
        for i in result:
            csv += str(i) + ","
        csv += "\n"
        ic += 1
    print >>f, csv
    f.close()
