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
img = cv.imread(r'Toeic3.png')
img = cv.resize(img, (944, 622))


cv.imshow('Image', img )
cv.waitKey(0)

height, width = img.shape[:2]

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


ret, thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY)

circles = cv.HoughCircles(thresh, cv.HOUGH_GRADIENT, 1, 8, param1=150, param2=8.5, minRadius=7, maxRadius=13)
circles = np.uint16(np.around(circles))
print(len(circles[0, :]))
ordoredCircleTemp = []

found = False

for i in circles[0, :]:
    circle = (i[0], i[1], 9)
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


ic = 1

for i in orderedCircle:
    jc = 1
    maxMean = 0
    maxMeanjc = 0
    maskIJ = np.zeros((height,width,3), np.uint8)
    for j in i:
        cv.circle(maskIJ, (j[0], j[1]), j[2], (255, 255, 255), -1)
    path = '.\Mask\mask'+str(ic)+".png"
    print(path)
    cv.imwrite(path, maskIJ)
    ic += 25
    if ic > 200 : ic -= 199
