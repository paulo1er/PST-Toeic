import cv2 as cv
import numpy as np
import math
from resize import resize


 

def solve(pathJPG, debug = False):

    width = 970
    height = 620

    img1 = cv.imread(pathJPG)

    img1 = resize(img1)
    img1 = cv.resize(img1, (width, height))
    
    if debug :
        cv.imshow('resized', img1)
        cv.waitKey(0)
    
   
    """
        
    on l'a deja brouillee, grisee etc??

    """

    gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

    blurred = cv.blur(gray, (5, 5))

    ret, thresh = cv.threshold(blurred, 170, 255, cv.THRESH_BINARY)

    if debug :
        cv.imshow('Image', img1)
        cv.waitKey(0)
        
    
        cv.imshow('Image', thresh)
        cv.waitKey(0)


    result = []
    alphaList = ['None', 'A', 'B', 'C', 'D']


    for i in range(1, 201, 1) :
        path = 'Mask/mask'+str(i)+".png"
        img3 = cv.imread(path, 0)

        img3 = cv.resize(img3, (width, height))

        ret, mask = cv.threshold(img3, 10, 255, cv.THRESH_BINARY)

        mask_inv = cv.bitwise_not(mask)

        img = cv.bitwise_and(img1, img1, mask=mask)
        img_tresh = cv.bitwise_not(cv.bitwise_and(thresh, thresh, mask=mask))

        circles = cv.HoughCircles(mask, cv.HOUGH_GRADIENT, 1, 8, param1=150, param2=8.5, minRadius=7, maxRadius=13)

        jc = 1
        maxMean = 0
        maxMeanjc = 0
        for j in circles[0, :]:
            cv.circle(img1, (j[0], j[1]), 9, (0, 255, 0), 1)

            width2 = [int(j[0] - 9), int(j[0] + 9)]
            height2 = [int(j[1] - 9), int(j[1] + 9)]

            if width2[0] < 0: width2[0] = 0
            if width2[1] > width: width2[1] = width
            if height2[0] < 0: height2[0] = 0
            if height2[1] > height: height2[1] = height

            roi = img_tresh[height2[0]:height2[1], width2[0]:width2[1]]

            if maxMean < cv.mean(roi)[0]:
                maxMean = cv.mean(roi)[0]
                maxMeanjc = jc
            jc += 1

        result.append(alphaList[maxMeanjc])


        if maxMeanjc != 0:
            tempJ = circles[0, :][maxMeanjc-1]
            cv.circle(img1, (tempJ[0], tempJ[1]), 9, (0, 0, 255), 1)

    if debug :
        cv.imshow('Image', img1)
        cv.waitKey(0)
  
    return result


if __name__ == '__main__':
    
    """
    import cProfile
 
    pr = cProfile.Profile()
    pr.enable()
    """ 
    result = solve(r'Grille_Toeic-15-1.jpg', True)
    """ 
    pr.disable()
     
    pr.print_stats(sort='cumtime')
    """
    

#ic=1
#for i in result:
#    print(str(ic) + ' : ' + str(i))
#    ic += 1
