# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
import numpy as np
import cv2 as cv
import math


def dist(point, org=(0, 0)):
    return math.sqrt(math.pow(point[0] - org[0], 2) + math.pow(point[1] - org[1], 2))


def circleSameRow(circle1, circle2):
    r = min(circle1[2], circle2[2])
    return circle2[1] - r < circle1[1] < circle2[1] + r


# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
img = cv.imread(r'Img\Toeic_scan.pdf\0_Toeic_scan.pdf.jpg')
img = cv.resize(img, (944, 622))

img2 = cv.imread(r'Img\Toeic_scan.pdf\1_Toeic_scan.pdf.jpg')
img2 = cv.resize(img, (944, 622))

cv.imshow('Image', img )
cv.waitKey(0)

height, width = img.shape[:2]

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
cv.waitKey(0)

blurred = cv.blur(gray, (2, 2))
cv.imshow('blurred', blurred)
cv.waitKey(0)

ret, thresh = cv.threshold(blurred,127,255,cv.THRESH_BINARY)
cv.imshow('thresh', thresh)
cv.waitKey(0)

circles = cv.HoughCircles(thresh, cv.HOUGH_GRADIENT, 1, 8, param1=200, param2=10.5, minRadius=7, maxRadius=11)
circles = np.uint16(np.around(circles))
print(len(circles[0, :]))
ordoredCircleTemp = []

found = False

for i in circles[0, :]:
    circle = (i[0], i[1], i[2])
    found = False
    for j in ordoredCircleTemp:
        if circleSameRow(j[0], circle):
            j.append(circle)
            found = True
    if not found:
        ordoredCircleTemp.append([circle])

orderedCircleTemp2 = []
orderedCircle = []
for i in ordoredCircleTemp:
    orderedCircleTemp2.append(sorted(i, key=lambda aCircle: aCircle[0]))

orderedCircleTemp2 = sorted(orderedCircleTemp2, key=lambda aCircle: aCircle[0][1])

c=0
for i in orderedCircleTemp2:
    for aCircle in i:
        if c==0 :
            orderedCircle.append([aCircle])
        else :
            orderedCircle[-1].append(aCircle)
        c += 1
        if c==4 :
            c=0



result = []
alphaList = ['None', 'A', 'B', 'C', 'D']

for i in orderedCircle:
    jc = 1
    maxMean = 0
    maxMeanjc = 0
    for j in i:
        cv.circle(img, (j[0], j[1]), j[2], (0, 255, 0), 1)


        width2 = [j[0] - j[2], j[0] + j[2]]
        height2 = [j[1] - j[2], j[1] + j[2]]
        if width2[0] < 0: width2[0] = 0
        if width2[1] > width: width2[1] = width
        if height2[0] < 0: height2[0] = 0
        if height2[1] > height: height2[1] = height

        roi = thresh[height2[0]:height2[1], width2[0]:width2[1]]

        if maxMean < cv.mean(roi)[0] and cv.mean(roi)[0]> 110:
            maxMean = cv.mean(roi)[0]
            maxMeanjc = jc
        jc += 1

    result.append(alphaList[maxMeanjc])
    if maxMeanjc != 0:
        j = i[maxMeanjc - 1]
        cv.circle(img, (j[0], j[1]), j[2], (0, 0, 255), 1)

finalResult = []
ic = 1
for i in result:
    finalResult.append([ic, i])
    ic += 25
    if ic > 200 : ic -= 199


finalResult = sorted(finalResult, key=lambda aItem: aItem[0])

for i in finalResult:
    print(str(i[0]) + ' : ' + str(i[1]))

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()

