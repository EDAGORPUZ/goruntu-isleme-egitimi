import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('helikopter.png', 0)
row, col = 600, 400
img = cv2.resize(img, (row, col))

ret, th1 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
#ret= return  th1=thresholding1

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,2)



cv2.imwrite('C:\\Users\\Eda\\Desktop\\helikopter.png', img )
cv2.imshow('original', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.waitKey(0)
cv2.destroyAllWindows()

