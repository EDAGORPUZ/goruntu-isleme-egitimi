import cv2
import numpy as np

img = cv2.imread('map.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3, 3))
ret, thresh = cv2.threshold(blur, 40, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = []

for i in range (len(contours)):
    hull.append(cv2.convexHull(contours[i], False)) #contourun değerlerinin indisi 
    #döndürülerek(false sayesinde) hull dizisinin içinde tutulur.

canvas = np.zeros((thresh.shape[0], thresh.shape[1],3), np.uint8)

for i in range (len(contours)):
    cv2.drawContours(canvas, contours, i, (255, 0, 0), 3, 8, hierarchy)
    cv2.drawContours(canvas, hull, i, (255, 0, 0), 1, 8)
    
    
cv2.imshow('orj', img)
cv2.imshow('image', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
    