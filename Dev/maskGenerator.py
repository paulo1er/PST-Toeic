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
img = cv.imread(r'img.png')

#cv.imshow('Image', cv.resize(img, (899 , 636)) )
#cv.waitKey(0)

width, height = img.shape[:2]

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray,127,255,cv.THRESH_BINARY)

circles = cv.HoughCircles(thresh, cv.HOUGH_GRADIENT, 1, 100, param1=50, param2=17.4, minRadius=38, maxRadius=50)
circles = np.uint16(np.around(circles))

midRadius=0
c=0
for circle in circles[0, :]:
    midRadius += circle[2]
    c += 1

midRadius = midRadius/c

print("midRadius = " + str(midRadius))

ordoredCircleTemp = []

found = False
for i in circles[0, :]:
    circle = (i[0], i[1], midRadius)
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
result = [0]*200
maxWidth=0

circle1= [0,0]
circle2= [0,0]
circle3= [0,0]
circle4= [0,0]

for i in orderedCircle:
    jc = 1
    maxMean = 0
    maxMeanjc = 0
    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    c = 0
    for j in i:
        cv.circle(img, (j[0], j[1]), j[2], (0, 0, 255), 15)
        x0 += j[0] - 42
        x1 += j[0] + 42
        if c == 0:
            y0 = j[1] - 42
            circle1[0] += j[0]
            circle1[1] += j[1]
        if c == 1:
            circle2[0] += j[0]
            circle2[1] += j[1]
        if c == 2:
            circle3[0] += j[0]
            circle3[1] += j[1]
        if c == 3:
            y1 = j[1] + 42
            circle4[0] += j[0]
            circle4[1] += j[1]
        c += 1

    result[ic-1] = [(x0, y0),(x1, y1)]

    if (y1 - y0) > maxWidth :
        maxWidth = y1 - y0

    ic += 25
    if ic > 200 : ic -= 199

circle1[0] = int(circle1[0]/200)
circle1[1] = int(circle1[1]/200)

circle2[0] = int(circle2[0]/200)
circle2[1] = int(circle2[1]/200)

circle3[0] = int(circle3[0]/200)
circle3[1] = int(circle3[1]/200)

circle4[0] = int(circle4[0]/200)
circle4[1] = int(circle4[1]/200)

mask_img = np.zeros((height,width,1), np.uint8)
circles = [circle1, circle2, circle3, circle4]
for circle in circles:
    cv.circle(mask_img, (circle[0], circle[1]), 42, (255, 255, 255), -1)
ret, mask = cv.threshold(mask_img, 170, 255, cv.THRESH_BINARY)


imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgGray, 170, 255, cv.THRESH_BINARY)


for i in range(0, 200, 1) :
    img_tresh = cv.bitwise_and(thresh,thresh, mask=mask)

    cv.imshow('Image', cv.resize(img_tresh, (899 , 636)))
    cv.waitKey(0)

print(maxWidth)
#print(result)

if False: '''
prenom
listening
reading

path = 'img.png'
cv.imwrite(path, img)

'''

if False: '''
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
'''
