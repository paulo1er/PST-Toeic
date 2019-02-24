import cv2 as cv
import numpy as np
from p2j import pdf2image
from resize import resize





#prend en entee le chemin vers un pdf et donne les reponses ABCD donnees
def getAnswers(filepath):
    n = pdf2image(filepath)
    """faudra penser a matcher la resolution de p2j avec celle de la photocopieuse"""
    results = []
    for i in range(n):
        print(i)
        pathJPG = "run/temp/out"+str(i)+".jpg"
        img = cv.imread(pathJPG)
        img = resize(img)
        cv.imwrite(pathJPG, img);
        results.append(solve(img, False))
    return results







def trouverLettre(part_img, coord, mask, circles, rayon, alphaList, section=0, debug=False):
    result=[]
    for i in range(0, 100, 1) :
       
        roi_color = part_img[coord['y1'][i]:coord['y2'][i], coord['x1'][i]:coord['x2'][i]]
    
        ret, thresh = cv.threshold(roi_color, 170, 255, cv.THRESH_BINARY)
    
        img_tresh = cv.bitwise_and(thresh,thresh, mask=mask)
    
        jc = 1
        minMeanjc = 0
        #minMean = 255
        doubleReponse = False
        for j in circles:
            width2 = [int(j[0] - rayon), int(j[0] + rayon)]
            height2 = [int(j[1] - rayon), int(j[1] + rayon)]
    
            roi = img_tresh[height2[0]:height2[1], width2[0]:width2[1]]
    
            if (cv.mean(roi)[0] < 115) and (not doubleReponse):
                if(minMeanjc != 0):
                    minMeanjc = 0
                    doubleReponse = True
                else:
                    #minMean = cv.mean(roi)[0]
                    minMeanjc = jc
            jc += 1
    
        if debug :
            cv.imshow(str(section+i), img_tresh)
            cv.waitKey(0)
            cv.destroyAllWindows()
    
        result.append(alphaList[minMeanjc])
    return result






def solve(img1, debug = False):
    #cv.imshow('Image', cv.resize(img1, (899 , 636)))
    #cv.waitKey(0)

    width, height = img1.shape[:2]
    #nom       = thresh[int(width*0.037386):int(width*0.074771), int(height*0.064528):int(height*0.473675)]
    #prenom    = thresh[int(width*0.037386):int(width*0.074771), int(height*0.595639):int(height*0.981209)]
    listening_color = img1[int(width*0.265768):int(width*0.966429), int(height*0.012143):int(height*0.481563)]
    reading_color   = img1[int(width*0.265768):int(width*0.966429), int(height*0.509484):int(height*0.978904)]


    listening = cv.cvtColor(listening_color, cv.COLOR_BGR2GRAY)
    reading = cv.cvtColor(reading_color, cv.COLOR_BGR2GRAY)

    if debug :
        cv.imshow('listening_color', cv.resize(listening_color, (899 , 636)))
        cv.imshow('reading_color', cv.resize(reading_color, (899 , 636)))
        cv.waitKey(0)

    result = []

    alphaList = ['None', 'A', 'B', 'C', 'D']
    coordonneListening = {
        "x1" : [83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859],
        "y1" : [1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118],
        "x2" : [283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059],
        "y2" : [41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158]
    }
    coordonneReading = {
        "x1" : [76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879],
        "y1" : [1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118],
        "x2" : [276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079],
        "y2" : [41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158]
    }

    width = 200
    height = 40
    rayon = 18
    circles = [[18,20], [72,20], [126,20], [181,20]]

   
    mask_img = np.zeros((height,width,1), np.uint8)

    for circle in circles:
        cv.circle(mask_img, (circle[0], circle[1]), rayon, (255, 255, 255), -1)

    ret, mask = cv.threshold(mask_img, 170, 255, cv.THRESH_BINARY)

    
    result=trouverLettre(listening, coordonneListening, mask, circles, rayon, alphaList, 0, debug)
    result+=trouverLettre(reading, coordonneReading, mask, circles, rayon, alphaList, 100, debug)
    
    
    print(result)
    return result


if __name__ == '__main__':

    """
    import cProfile

    pr = cProfile.Profile()
    pr.enable()
    """
    image=img = cv.imread(r'run\temp\out2.jpg')
    result = solve(image, True  )
    """
    pr.disable()

    pr.print_stats(sort='cumtime')
    """


#ic=1
#for i in result:
#    print(str(ic) + ' : ' + str(i))
#    ic += 1
