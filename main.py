from Interface import interface
from p2j import pdf2image
from solve import solve
from export import export
from score import compareAll




#prend en entée le chemin vers un pdf et donne les réponses ABCD données
def getAnswers(filepath):
    n = pdf2image(filepath)
    
    results = []
    for i in range(n):
        print(i)
        pathJPG = "temp/out"+str(i)+".jpg"
        results.append(solve(pathJPG))
    return results




def main():
    filepathCorr = interface("Choisir le pdf du corrigé")  #si aucun doc choisi : probleme
    filepathEleves = interface("Choisir le pdf des copies")
    
    
    answersCorr=getAnswers(filepathCorr)[0]
    answersEleves=getAnswers(filepathEleves)
    #print("answersCorr : "+str(answersCorr))
    #print("answersEleves : "+str(answersEleves))
    scores=compareAll(answersCorr,answersEleves)
    
    
    print("scores : "+str(scores))
    
    export(scores)


import cProfile
 
pr = cProfile.Profile()
pr.enable()
 
main()
 
pr.disable()
 
pr.print_stats(sort='cumtime')