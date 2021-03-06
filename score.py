# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 18:07:30 2019

@author: Guillaume
"""


"""
This file contains functions to calculate the score of the students and the statistics for the group

"""


def average(lst): 
    return sum(lst) / len(lst) 


# calculates the statistics for the class
def getStats(liste):
    
    # average for each question
    percentages=[0 for i in range(200)]
    for question in range(200):
        for eleve in range(len(liste)):
            percentages[question]+=liste[eleve][question]
    for question in range(200):
        percentages[question] = 100*percentages[question]/len(liste)

    # average for each exercise
    exercisesRes=[average(percentages[:6]),
                  average(percentages[7:31]),
                  average(percentages[32:70]),
                  average(percentages[71:100]),
                                                      
                  average(percentages[101:130]),
                  average(percentages[131:146]),
                  average(percentages[147:175]),
                  average(percentages[176:200])   ]
    # add the number of points of the question
    nbQuestions = [ 6,25,39,30,30,16,29,25 ]
    for i in range(8):
        exercisesRes[i]='="'+ str(float(nbQuestions[i]*exercisesRes[i])/100.) + ' / ' + str(nbQuestions[i])+'"'
    
    return exercisesRes, percentages




# given the correction, marks every answer of ONE student as either true or false
def compare2(correction,answers):
    # how we calculate the score 
    tableListening=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,15,20,25,30,35,40,45,50,55,60,70,80,85,90,95,100,105,115,125,135,140,150,160,170,175,180,190,200,205,215,220,225,230,235,245,255,260,265,275,285,290,295,300,310,320,325,330,335,340,345,350,355,360,365,370,375,385,395,400,405,415,420,425,430,435,440,445,450,455,460,465,475,480,485,490,495,495,495,495,495,495,495,495]
    tableReading=  [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,15,20,25,30,35,40,45,55,60,65,70,75,80,85,90,95,105,115,120,125,130,135,140,145,155,160,170,175,185,195,205,210,215,220,230,240,245,250,255,260,270,275,280,285,290,295,295,300,310,315,320,325,330,335,340,345,355,360,370,375,385,390,395,400,405,415,420,425,435,440,450,455,460,470,475,485,485,490,495]
    listeningNb=0
    readingNb=0
    
    nbQuestions = [ 6,25,39,30,30,16,29,25 ]

    trueFalseList=[0 for i in range(200)]
    
    for i in range(len(correction)):
        if correction[i]==answers[i]:
            #list containing the number of points at each question (0 or 1)
            trueFalseList[i]=1        

    
    #number of correct answers at each exercise
    exercisesNb=[
        sum(trueFalseList[:6]),
        sum(trueFalseList[6:31]),
        sum(trueFalseList[31:70]),
        sum(trueFalseList[70:100]),
                                              
        sum(trueFalseList[100:130]),
        sum(trueFalseList[130:146]),
        sum(trueFalseList[146:175]),
        sum(trueFalseList[175:200])   
        ] 
    
    #nb of correct answers in each section 
    listeningNb = sum(exercisesNb[:4])
    readingNb = sum(exercisesNb[4:])
           
    #score over 495 in each section 
    listeningScore=tableListening[listeningNb]
    readingScore=tableReading[readingNb]

    for i in range(8):
        exercisesNb[i] ='="'+ str(exercisesNb[i]) + ' / ' + str(nbQuestions[i])+'"'
        
    total=listeningScore+readingScore
    result = [total, listeningScore,readingScore]+exercisesNb
    return result,trueFalseList




# main function : given the correction, marks every answer of every student as either true or false 
def compareAll(correction,answers):
    resultsList=[]
    trueFalseLists=[]
    # loop over the students
    for j in answers:
        compare=compare2(correction,j)
        resultsList.append(compare[0])
        trueFalseLists.append(compare[1])
    
    # get the statistics of the students
    stats=getStats(trueFalseLists)
    
    # calculate average of the class for total and both sectionsn score
    scoreMoy=average([res[0] for res in resultsList])
    listeningMoy=average([res[1] for res in resultsList])
    readingMoy=average([res[2] for res in resultsList])
    moyennes=[scoreMoy, listeningMoy, readingMoy]
    
    return resultsList,moyennes+stats[0], stats[1]





# main for testing only
if __name__ == '__main__':
    corr=['D', 'C', 'A', 'D', 'B', 'C', 'B', 'D', 'A', 'C', 'D', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'C', 'C', 'B', 'D', 'A', 'C', 'D', 'D', 'A', 'B', 'D', 'A', 'C', 'C', 'D', 'B', 'B', 'D', 'B', 'C', 'D', 'B', 'C', 'A', 'B', 'A', 'C', 'C', 'D', 'B', 'D', 'D', 'A', 'B', 'C', 'B', 'A', 'B', 'C', 'D', 'C', 'A', 'C', 'D', 'A', 'A', 'D', 'D', 'B', 'C', 'B', 'C', 'B', 'D', 'C', 'B', 'A', 'D', 'A', 'C', 'C', 'C', 'B', 'D', 'D', 'C', 'C', 'B', 'B', 'A', 'C', 'C', 'D', 'D', 'A', 'A', 'B', 'C', 'A', 'B', 'C', 'D',      'C', 'C', 'B', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'C', 'C', 'B', 'B', 'C', 'C', 'C', 'B', 'A', 'B', 'A', 'B', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'A', 'A', 'C', 'B', 'B', 'A', 'C', 'A', 'B', 'C', 'B', 'B', 'C', 'B', 'C', 'A', 'B', 'C', 'C', 'B', 'A', 'C', 'C', 'A', 'B', 'A', 'B', 'A', 'A', 'C', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'D', 'B']
    ans= ['C', 'C', 'A', 'C', 'C', 'B', 'D', 'C', 'B', 'C', 'C', 'C', 'D', 'B', 'C', 'D', 'B', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'D', 'A', 'A', 'C', 'A', 'B', 'D', 'C', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'C', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'C', 'A', 'D', 'C', 'C', 'C', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'C', 'D', 'B', 'A', 'A', 'C', 'B', 'B', 'D', 'D', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'C', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'C', 'A', 'A', 'D',      'C', 'D', 'A', 'D', 'D', 'C', 'C', 'C', 'C', 'C', 'B', 'C', 'D', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'A', 'A', 'D', 'B', 'B', 'C', 'C', 'D', 'D', 'C', 'A', 'A', 'B', 'D', 'D', 'D', 'D', 'C', 'D', 'D', 'C', 'A', 'A', 'D', 'C', 'A', 'D', 'D', 'A', 'B', 'C', 'B', 'B', 'A', 'B', 'D', 'A', 'A', 'A', 'A', 'D', 'B', 'B', 'D', 'B', 'D', 'A', 'C', 'D', 'D', 'B', 'A', 'B', 'A', 'C', 'C', 'B', 'C', 'C', 'C', 'A', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'C', 'B', 'B', 'A', 'A', 'A']
    ans2=['D', 'C', 'A', 'D', 'B', 'C', 'D', 'C', 'B', 'C', 'C', 'C', 'D', 'B', 'C', 'D', 'B', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'D', 'A', 'A', 'C', 'A', 'B', 'D', 'C', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'C', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'C', 'A', 'D', 'C', 'C', 'C', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'C', 'D', 'B', 'A', 'A', 'C', 'B', 'B', 'D', 'D', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'C', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'C', 'A', 'A', 'D',      'C', 'D', 'A', 'D', 'D', 'C', 'C', 'C', 'C', 'C', 'B', 'C', 'D', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'A', 'A', 'D', 'B', 'B', 'C', 'C', 'D', 'D', 'C', 'A', 'A', 'B', 'D', 'D', 'D', 'D', 'C', 'D', 'D', 'C', 'A', 'A', 'D', 'C', 'A', 'D', 'D', 'A', 'B', 'C', 'B', 'B', 'A', 'B', 'D', 'A', 'A', 'A', 'A', 'D', 'B', 'B', 'D', 'B', 'D', 'A', 'C', 'D', 'D', 'B', 'A', 'B', 'A', 'C', 'C', 'B', 'C', 'C', 'C', 'A', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'C', 'B', 'B', 'A', 'A', 'A']
    ans3=['A', 'C', 'A', 'D', 'B', 'C', 'B', 'C', 'B', 'C', 'C', 'C', 'D', 'B', 'C', 'D', 'B', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'D', 'A', 'A', 'C', 'A', 'B', 'D', 'C', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'C', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'C', 'A', 'D', 'C', 'C', 'C', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'C', 'D', 'B', 'A', 'A', 'C', 'B', 'B', 'D', 'D', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'C', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'C', 'A', 'A', 'D',      'C', 'D', 'A', 'D', 'D', 'C', 'C', 'C', 'C', 'C', 'B', 'C', 'D', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'A', 'A', 'D', 'B', 'B', 'C', 'C', 'D', 'D', 'C', 'A', 'A', 'B', 'D', 'D', 'D', 'D', 'C', 'D', 'D', 'C', 'A', 'A', 'D', 'C', 'A', 'D', 'D', 'A', 'B', 'C', 'B', 'B', 'A', 'B', 'D', 'A', 'A', 'A', 'A', 'D', 'B', 'B', 'D', 'B', 'D', 'A', 'C', 'D', 'D', 'B', 'A', 'B', 'A', 'C', 'C', 'B', 'C', 'C', 'C', 'A', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'C', 'B', 'B', 'A', 'A', 'A']
   
    test=compareAll(corr,[ans,ans2,ans3])
    #print(test [0])
    #print(test [1])
    #print(test [2])
    from export import exportIndiv, exportClasse
    exportIndiv(test[0], [("tata"),("tété"),("titi"),("tutu"),("tonton"),("toto"),("tyty")])
    exportClasse(test[1],test[2])