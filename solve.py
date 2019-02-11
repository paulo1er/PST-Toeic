import cv2 as cv
import numpy as np
import math
from resize import resize
import pickle



def solve(pathJPG, debug = False):

    img1 = cv.imread(pathJPG)

    width, height = img1.shape[:2]
    img1 = img1[100:width-100, 100:height-100]
    img1 = resize(img1)

    #cv.imshow('Image', cv.resize(img1, (899 , 636)))
    #cv.waitKey(0)

    width, height = img1.shape[:2]
    #nom       = thresh[int(width*0.037386):int(width*0.074771), int(height*0.064528):int(height*0.473675)]
    #prenom    = thresh[int(width*0.037386):int(width*0.074771), int(height*0.595639):int(height*0.981209)]
    listening_color = img1[int(width*0.265768):int(width*0.966429), int(height*0.012143):int(height*0.481563)]
    reading_color   = img1[int(width*0.265768):int(width*0.966429), int(height*0.509484):int(height*0.978904)]


    listening = cv.cvtColor(listening_color, cv.COLOR_BGR2GRAY)
    reading = cv.cvtColor(reading_color, cv.COLOR_BGR2GRAY)
    '''
    if debug :
        cv.imshow('listening_color', cv.resize(listening_color, (899 , 636)))
        cv.imshow('reading_color', cv.resize(reading_color, (899 , 636)))
        cv.waitKey(0)
    '''

    result = []

    alphaList = ['None', 'A', 'B', 'C', 'D']
    coordonneListening = {
          "x1" : [191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,191,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,805,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,1420,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070,2070 ],
          "y1" : [4,114,226,337,447,558,669,780,891,1002,1113,1223,1333,1444,1555,1666,1777,1888,1999,2110,2220,2332,2442,2553,2663,4,114,226,337,447,558,669,780,891,1002,1113,1223,1333,1444,1555,1666,1777,1888,1999,2110,2220,2332,2442,2553,2663,4,114,226,337,447,558,669,780,891,1002,1113,1223,1333,1444,1555,1666,1777,1888,1999,2110,2220,2332,2442,2553,2663,4,114,226,337,447,558,669,780,891,1002,1113,1223,1333,1444,1555,1666,1777,1888,1999,2110,2220,2332,2442,2553,2663],
          "x2" : [681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,681,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1295,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,1910,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560,2560],
          "y2" : [95,205,317,428,538,649,760,871,982,1093,1204,1314,1424,1535,1646,1757,1868,1979,2090,2201,2311,2423,2533,2644,2754,95,205,317,428,538,649,760,871,982,1093,1204,1314,1424,1535,1646,1757,1868,1979,2090,2201,2311,2423,2533,2644,2754,95,205,317,428,538,649,760,871,982,1093,1204,1314,1424,1535,1646,1757,1868,1979,2090,2201,2311,2423,2533,2644,2754,95,205,317,428,538,649,760,871,982,1093,1204,1314,1424,1535,1646,1757,1868,1979,2090,2201,2311,2423,2533,2644,2754]
    }
    coordonneReanding = {
          "x1" : [180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,180,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,823,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,1474,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115,2115],
          "y1" : [0,111,222,333,444,555,666,777,888,999,1110,1221,1332,1443,1554,1665,1776,1887,1998,2109,2220,2331,2442,2553,2664,0,111,222,333,444,555,666,777,888,999,1110,1221,1332,1443,1554,1665,1776,1887,1998,2109,2220,2331,2442,2553,2664,0,111,222,333,444,555,666,777,888,999,1110,1221,1332,1443,1554,1665,1776,1887,1998,2109,2220,2331,2442,2553,2664,0,111,222,333,444,555,666,777,888,999,1110,1221,1332,1443,1554,1665,1776,1887,1998,2109,2220,2331,2442,2553,2664],
          "x2" : [670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,670,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1313,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,1964,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605,2605],
          "y2" : [91,202,313,424,535,646,757,868,979,1090,1201,1312,1423,1534,1645,1756,1867,1978,2089,2200,2311,2422,2533,2644,2755,91,202,313,424,535,646,757,868,979,1090,1201,1312,1423,1534,1645,1756,1867,1978,2089,2200,2311,2422,2533,2644,2755,91,202,313,424,535,646,757,868,979,1090,1201,1312,1423,1534,1645,1756,1867,1978,2089,2200,2311,2422,2533,2644,2755,91,202,313,424,535,646,757,868,979,1090,1201,1312,1423,1534,1645,1756,1867,1978,2089,2200,2311,2422,2533,2644,2755]
    }

    width = 490
    height = 91
    circles = [[42,46], [176,46], [309,46], [444,46]]

    ret, thresh = cv.threshold(listening_color, 170, 255, cv.THRESH_BINARY)

    mask_img = np.zeros((height,width,1), np.uint8)

    for circle in circles:
        cv.circle(mask_img, (circle[0], circle[1]), 42, (255, 255, 255), -1)


    ret, mask = cv.threshold(mask_img, 170, 255, cv.THRESH_BINARY)

    for i in range(0, 100, 1) :
        #print(str(i+1) +"/200")
        roi_color = listening[coordonneListening['y1'][i]:coordonneListening['y2'][i], coordonneListening['x1'][i]:coordonneListening['x2'][i]]

        ret, thresh = cv.threshold(roi_color, 170, 255, cv.THRESH_BINARY)

        img_tresh = cv.bitwise_and(thresh,thresh, mask=mask)



        jc = 1
        minMean = 255
        minMeanjc = 0
        for j in circles:
            width2 = [int(j[0] - 42), int(j[0] + 42)]
            height2 = [int(j[1] - 42), int(j[1] + 42)]

            roi = img_tresh[height2[0]:height2[1], width2[0]:width2[1]]

            if (minMean > cv.mean(roi)[0]) and (cv.mean(roi)[0] != 0):
                minMean = cv.mean(roi)[0]
                minMeanjc = jc
            jc += 1

        if debug :
            cv.imshow(str(i+1)+" : "+alphaList[minMeanjc], img_tresh)
            cv.waitKey(0)

        result.append(alphaList[minMeanjc])

    ret, thresh = cv.threshold(reading_color, 170, 255, cv.THRESH_BINARY)

    for i in range(0, 100, 1) :
        #print(str(i+101) +"/200")
        roi_color = reading[coordonneReanding['y1'][i]:coordonneReanding['y2'][i], coordonneReanding['x1'][i]:coordonneReanding['x2'][i]]

        ret, thresh = cv.threshold(roi_color, 170, 255, cv.THRESH_BINARY)

        img_tresh = cv.bitwise_and(thresh,thresh, mask=mask)



        jc = 1
        minMean = 255
        minMeanjc = 0
        for j in circles:
            width2 = [int(j[0] - 42), int(j[0] + 42)]
            height2 = [int(j[1] - 42), int(j[1] + 42)]

            roi = img_tresh[height2[0]:height2[1], width2[0]:width2[1]]

            if (minMean > cv.mean(roi)[0]) and (cv.mean(roi)[0] != 0):
                minMean = cv.mean(roi)[0]
                minMeanjc = jc
            jc += 1

        if debug :
            cv.imshow(str(i+101)+" : "+alphaList[minMeanjc], img_tresh)
            cv.waitKey(0)

        result.append(alphaList[minMeanjc])



    if False : '''
    # listening
    ret, thresh = cv.threshold(listening_color, 170, 255, cv.THRESH_BINARY)

    for i in range(1, 101, 1) :
        print(str(i) +"/200")
        width, height = thresh.shape[:2]

        path = 'Mask/mask'+str(i)+".pckl"
        f = open(path, 'rb')
        const = pickle.load(f)
        f.close()
        mask = const["mask"]
        circles = const["circles"]
        img_tresh = cv.bitwise_and(thresh,thresh, mask=mask)

        jc = 1
        minMean = 255
        minMeanjc = 0
        for j in circles[0, :]:
            cv.circle(listening_color, (j[0], j[1]), 42, (0, 255, 0), 15)

            width2 = [int(j[0] - 42), int(j[0] + 42)]
            height2 = [int(j[1] - 42), int(j[1] + 42)]

            #if width2[0] < 0: width2[0] = 0
            #if width2[1] > width: width2[1] = width
            #if height2[0] < 0: height2[0] = 0
            #if height2[1] > height: height2[1] = height

            roi = img_tresh[height2[0]:height2[1], width2[0]:width2[1]]

            if (minMean > cv.mean(roi)[0]) and (cv.mean(roi)[0] != 0):
                minMean = cv.mean(roi)[0]
                minMeanjc = jc
            jc += 1
        #cv.waitKey(0)

        result.append(alphaList[minMeanjc])


        if minMeanjc != 0:
            tempJ = circles[0, :][minMeanjc-1]
            cv.circle(listening_color, (tempJ[0], tempJ[1]), 42, (0, 0, 255), 15)

    if debug :
        cv.imshow('Image', cv.resize(listening_color, (899 , 636)))
        cv.waitKey(0)

    # reading
    ret, thresh = cv.threshold(reading_color, 170, 255, cv.THRESH_BINARY)

    for i in range(101, 201, 1) :
        print(str(i) +"/200")
        width, height = thresh.shape[:2]

        path = 'Mask/mask'+str(i)+".pckl"
        f = open(path, 'rb')
        const = pickle.load(f)
        f.close()
        mask = const["mask"]
        circles = const["circles"]
        img_tresh = cv.bitwise_and(thresh,thresh, mask=mask)

        jc = 1
        minMean = 255
        minMeanjc = 0
        for j in circles[0, :]:
            cv.circle(reading_color, (j[0], j[1]), 42, (0, 255, 0), 15)

            width2 = [int(j[0] - 42), int(j[0] + 42)]
            height2 = [int(j[1] - 42), int(j[1] + 42)]

            #if width2[0] < 0: width2[0] = 0
            #if width2[1] > width: width2[1] = width
            #if height2[0] < 0: height2[0] = 0
            #if height2[1] > height: height2[1] = height

            roi = img_tresh[height2[0]:height2[1], width2[0]:width2[1]]

            if (minMean > cv.mean(roi)[0]) and (cv.mean(roi)[0] != 0):
                minMean = cv.mean(roi)[0]
                minMeanjc = jc
            jc += 1
        #cv.waitKey(0)

        result.append(alphaList[minMeanjc])


        if minMeanjc != 0:
            tempJ = circles[0, :][minMeanjc-1]
            cv.circle(reading_color, (tempJ[0], tempJ[1]), 42, (0, 0, 255), 15)

    if debug :
        cv.imshow('Image', cv.resize(reading_color, (899 , 636)))
        cv.waitKey(0)
    '''
    print(result)
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
