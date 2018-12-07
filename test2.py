import cv2 as cv
import numpy as np
import math


def dist(point, org=(0, 0)):
    return math.sqrt(math.pow(point[0] - org[0], 2) + math.pow(point[1] - org[1], 2))


def circleSameRow(circle1, circle2):
    r = min(circle1[2], circle2[2])
    return circle2[1] - r < circle1[1] < circle2[1] + r


def resize(img):
    width, height = img.shape[:2]

    blurred = cv.GaussianBlur(img, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 5, 2)

    lines = cv.HoughLinesP(thresh, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

    top_left = (lines[0][0][0], lines[0][0][1])
    bottom_right = (lines[0][0][0], lines[0][0][1])
    bottom_left = (lines[0][0][0], lines[0][0][1])
    top_right = (lines[0][0][0], lines[0][0][1])

    for line in lines:
        x1, y1, x2, y2 = line[0]

        if dist((x1, y1)) < dist(top_left):
            top_left = (x1, y1)
        if dist((x2, y2)) < dist(top_left):
            top_left = (x2, y2)

        if dist((x1, y1)) > dist(bottom_right):
            bottom_right = (x1, y1)
        if dist((x2, y2)) > dist(bottom_right):
            bottom_right = (x2, y2)

        if dist((x1, y1), (0, width)) < dist(bottom_left, (0, width)):
            bottom_left = (x1, y1)
        if dist((x2, y2), (0, width)) < dist(bottom_left, (0, width)):
            bottom_left = (x2, y2)

        if dist((x1, y1), (0, width)) > dist(top_right, (0, width)):
            top_right = (x1, y1)
        if dist((x2, y2), (0, width)) > dist(top_right, (0, width)):
            top_right = (x2, y2)

    pts1 = np.float32([top_left, bottom_left, top_right, bottom_right])
    pts2 = np.float32([[0, 0], [0, width], [height, 0], [height, width]])

    M = cv.getPerspectiveTransform(pts1, pts2)

    return cv.warpPerspective(img, M, (height, width))


width = 944
height = 622

img1 = cv.imread(r'Img\Toeic_scan.pdf\0_Toeic_scan.pdf.jpg')

img1 = resize(img1)
img1 = cv.resize(img1, (width, height))

gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

blurred = cv.blur(gray, (5, 5))

ret, thresh = cv.threshold(blurred, 170, 255, cv.THRESH_BINARY)

cv.imshow('Image', img1)
cv.waitKey(0)

cv.imshow('Image', thresh)
cv.waitKey(0)

img3 = cv.imread(r'Img\Toeic3.png', 0)

img3 = cv.resize(img3, (width, height))

ret, mask = cv.threshold(img3, 10, 255, cv.THRESH_BINARY)

mask_inv = cv.bitwise_not(mask)

img = cv.bitwise_and(img1, img1, mask=mask)
img_tresh = cv.bitwise_not(cv.bitwise_and(thresh, thresh, mask=mask))

cv.imshow('Image', img)
cv.waitKey(0)

cv.imshow('Image', img_tresh)
cv.waitKey(0)

circles = cv.HoughCircles(mask, cv.HOUGH_GRADIENT, 1, 8, param1=200, param2=10.5, minRadius=7, maxRadius=11)

circles = np.uint16(np.around(circles))
print(len(circles[0, :]))
ordoredCircleTemp = []

found = False

for i in circles[0, :]:
    circle = (i[0], i[1], 8)
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

c = 0
for i in orderedCircleTemp2:
    for aCircle in i:
        if c == 0:
            orderedCircle.append([aCircle])
        else:
            orderedCircle[-1].append(aCircle)
        c += 1
        if c == 4:
            c = 0

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
        if width2[0] < 0 :
            width2[0] = 0
        if width2[1] > width :
            width2[1] = width
        if height2[0] < 0 :
            height2[0] = 0
        if height2[1] > height :
            height2[1] = height

        roi = img_tresh[height2[0]:height2[1], width2[0]:width2[1]]

        if maxMean <= cv.mean(roi)[0]:
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
    if ic > 200: ic -= 199

finalResult = sorted(finalResult, key=lambda aItem: aItem[0])

for i in finalResult:
    print(str(i[0]) + ' : ' + str(i[1]))

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
