from Interface import interface1
from p2j import pdf2image
from solve import solve
from export import exportIndiv,exportClasse,exportAnswersEleves
from score import compareAll
import cv2
from resize import resize
from name import promptNames

#prend en entee le chemin vers un pdf et donne les reponses ABCD donnees
def getAnswers(filepath):
    n = pdf2image(filepath)
    """faudra penser a matcher la resolution de p2j avec celle de la photocopieuse"""
    results = []
    for i in range(n):
        print(i)
        pathJPG = "run/temp/out"+str(i)+".jpg"
        img = cv2.imread(pathJPG)
        img = resize(img)
        cv2.imwrite(pathJPG, img);
        results.append(solve(img,False))
    return results




def main():
    filepathCorr,filepathEleves = interface1();
    #filepathCorr = interface("Choisir le pdf du corrige")  #si aucun doc choisi : probleme
    #filepathEleves = interface("Choisir le pdf des copies")


    answersCorr=getAnswers(filepathCorr)[0]
    answersEleves=getAnswers(filepathEleves)
    #print("answersCorr : "+str(answersCorr))
    #print("answersEleves : "+str(answersEleves))
    scores=compareAll(answersCorr,answersEleves)
    names = promptNames()
    print(names)
    print("scores : ")
    for i in scores:
        print(i)



    exportIndiv(scores[0], names)
    exportClasse(scores[1],scores[2])
    exportAnswersEleves(answersEleves, names)

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
