import cv2 as cv
import numpy as np




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
        cv.imwrite("run/listening_color.jpg", listening_color);
        cv.imshow('reading_color', cv.resize(reading_color, (899 , 636)))
        cv.imwrite("run/reading_color.jpg", reading_color);
        cv.waitKey(0)

    result = []

    alphaList = ['None', 'A', 'B', 'C', 'D']
    coordonneListening = {
        "x1" : [83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,335,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,590,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859,859],
        "y1" : [1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118],
        "x2" : [283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,283,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,535,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,790,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059,1059],
        "y2" : [41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158]
    }
    coordonneReanding = {
        "x1" : [76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,342,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,610,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879,879],
        "y1" : [1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118,1,48,94,141,187,234,280,327,373,420,466,513,560,606,653,699,746,792,839,885,932,978,1025,1071,1118],
        "x2" : [276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,276,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,542,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,810,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079,1079],
        "y2" : [41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158,41,88,134,181,227,274,320,367,413,460,506,553,600,646,693,739,786,832,879,925,972,1018,1065,1111,1158]
    }

    width = 200
    height = 40
    rayon = 18
    circles = [[18,20], [72,20], [126,20], [181,20]]

    ret, thresh = cv.threshold(listening_color, 170, 255, cv.THRESH_BINARY)

    mask_img = np.zeros((height,width,1), np.uint8)

    for circle in circles:
        cv.circle(mask_img, (circle[0], circle[1]), rayon, (255, 255, 255), -1)


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
            width2 = [int(j[0] - rayon), int(j[0] + rayon)]
            height2 = [int(j[1] - rayon), int(j[1] + rayon)]

            roi = img_tresh[height2[0]:height2[1], width2[0]:width2[1]]

            if (minMean > cv.mean(roi)[0]) and (cv.mean(roi)[0] != 0):
                minMean = cv.mean(roi)[0]
                minMeanjc = jc
            jc += 1

        if debug :
            cv.circle(img_tresh, (circles[minMeanjc-1][0], circles[minMeanjc-1][1]), rayon, (0, 0, 255), 5)
            cv.imshow("img", img_tresh)
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
            width2 = [int(j[0] - rayon), int(j[0] + rayon)]
            height2 = [int(j[1] - rayon), int(j[1] + rayon)]

            roi = img_tresh[height2[0]:height2[1], width2[0]:width2[1]]

            if (minMean > cv.mean(roi)[0]) and (cv.mean(roi)[0] != 0):
                minMean = cv.mean(roi)[0]
                minMeanjc = jc
            jc += 1

        if debug :
            cv.circle(img_tresh, (circles[minMeanjc-1][0], circles[minMeanjc-1][1]), rayon, (0, 0, 255), 5)
            cv.imshow("img", img_tresh)
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
