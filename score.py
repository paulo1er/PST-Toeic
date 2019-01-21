# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 18:07:30 2019

@author: Guillaume
"""

def compareAll(correction,answers):
    res=[]
    for j in answers:
        res.append(compare2(correction,j))
    return res

def compare2(correction,answers):
    
    tableListening=[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,15,20,25,30,35,40,45,50,55,60,70,80,85,90,95,100,105,115,125,135,140,150,160,170,175,180,190,200,205,215,220,225,230,235,245,255,260,265,275,285,290,295,300,310,320,325,330,335,340,345,350,355,360,365,370,375,385,395,400,405,415,420,425,430,435,440,445,450,455,460,465,475,480,485,490,495,495,495,495,495,495,495,495]
    tableReading=  [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,10,15,20,25,30,35,40,45,55,60,65,70,75,80,85,90,95,105,115,120,125,130,135,140,145,155,160,170,175,185,195,205,210,215,220,230,240,245,250,255,260,270,275,280,285,290,295,295,300,310,315,320,325,330,335,340,345,355,360,370,375,385,390,395,400,405,415,420,425,435,440,450,455,460,470,475,485,485,490,495]
    listeningNb=0
    readingNb=0
    
    listeningParts = [ ["Description d'images",6] , ['Question-Response',25] , ['Dialogues',39] , ['Discussions - Annonces',30] ]
    readingParts = [ ['Phrases à compléter',30] , ['Textes à compléter',16] , ['Lecture contenus redirigés,  Passages simples',29],['Lecture contenus redirigés, Passages multiples', 25] ]
    listPartsNb = [ 0, 0, 0, 0 ]
    readPartsNb = [ 0, 0, 0, 0 ]
	
    for i in range(len(correction)):
        if correction[i]==answers[i]:
                if i<100:
                    listeningNb+=1
                    if i<6:
                        listPartsNb[0]+=1
                    elif i<6+25:
                        listPartsNb[1]+=1
                    elif i<6+25+39:
                        listPartsNb[2]+=1
                    else:
                        listPartsNb[3]+=1
                else:
                    readingNb+=1
                    if i<30:
                        readPartsNb[0]+=1
                    elif i<30+16:
                        readPartsNb[1]+=1
                    elif i<30+16+29:
                        readPartsNb[2]+=1
                    else:
                        readPartsNb[3]+=1
                        
    listeningScore=tableListening[listeningNb]
    readingScore=tableReading[readingNb]
    
    for i in range(4):
        listPartsNb[i] = str(listPartsNb[i]) + ' / ' + str(listeningParts[i][1])
        readPartsNb[i] = str(readPartsNb[i]) + ' / ' + str(readingParts[i][1])
    
    result = [listeningScore+readingScore,listeningScore, readingScore] + listPartsNb + readPartsNb
    return result



if __name__ == '__main__':
    corr=['D', 'C', 'A', 'D', 'B', 'C', 'B', 'D', 'A', 'C', 'D', 'B', 'A', 'C', 'D', 'B', 'C', 'D', 'C', 'C', 'B', 'D', 'A', 'C', 'D', 'D', 'A', 'B', 'D', 'A', 'C', 'C', 'D', 'B', 'B', 'D', 'B', 'C', 'D', 'B', 'C', 'A', 'B', 'A', 'C', 'C', 'D', 'B', 'D', 'D', 'A', 'B', 'C', 'B', 'A', 'B', 'C', 'D', 'C', 'A', 'C', 'D', 'A', 'A', 'D', 'D', 'B', 'C', 'B', 'C', 'B', 'D', 'C', 'B', 'A', 'D', 'A', 'C', 'C', 'C', 'B', 'D', 'D', 'C', 'C', 'B', 'B', 'A', 'C', 'C', 'D', 'D', 'A', 'A', 'B', 'C', 'A', 'B', 'C', 'D',      'C', 'C', 'B', 'C', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'A', 'A', 'C', 'C', 'B', 'B', 'C', 'C', 'C', 'B', 'A', 'B', 'A', 'B', 'C', 'A', 'B', 'A', 'C', 'D', 'B', 'A', 'A', 'C', 'B', 'B', 'A', 'C', 'A', 'B', 'C', 'B', 'B', 'C', 'B', 'C', 'A', 'B', 'C', 'C', 'B', 'A', 'C', 'C', 'A', 'B', 'A', 'B', 'A', 'A', 'C', 'A', 'B', 'A', 'A', 'C', 'A', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'A', 'A', 'A', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'B', 'A', 'D', 'B']
    ans= ['C', 'C', 'A', 'C', 'C', 'B', 'D', 'C', 'B', 'C', 'C', 'C', 'D', 'B', 'C', 'D', 'B', 'C', 'A', 'C', 'C', 'C', 'A', 'B', 'D', 'A', 'A', 'C', 'A', 'B', 'D', 'C', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'C', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'C', 'A', 'D', 'C', 'C', 'C', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B', 'A', 'A', 'A', 'C', 'D', 'B', 'A', 'A', 'C', 'B', 'B', 'D', 'D', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'C', 'A', 'A', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'B', 'C', 'A', 'A', 'D',      'C', 'D', 'A', 'D', 'D', 'C', 'C', 'C', 'C', 'C', 'B', 'C', 'D', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'A', 'A', 'D', 'B', 'B', 'C', 'C', 'D', 'D', 'C', 'A', 'A', 'B', 'D', 'D', 'D', 'D', 'C', 'D', 'D', 'C', 'A', 'A', 'D', 'C', 'A', 'D', 'D', 'A', 'B', 'C', 'B', 'B', 'A', 'B', 'D', 'A', 'A', 'A', 'A', 'D', 'B', 'B', 'D', 'B', 'D', 'A', 'C', 'D', 'D', 'B', 'A', 'B', 'A', 'C', 'C', 'B', 'C', 'C', 'C', 'A', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'A', 'A', 'C', 'C', 'A', 'C', 'B', 'B', 'A', 'A', 'A']
   
    print(compareAll(corr,[ans]))
