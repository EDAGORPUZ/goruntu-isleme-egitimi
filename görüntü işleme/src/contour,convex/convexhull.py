import cv2
import numpy as np

img = cv2.imread('map.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(gray, (3, 3))
ret, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
#thresh için ilk alt değeri 75 girmiştik fakat afrika gözükmediği için manuel olarak
#düşürerek 50 gibi derğerlere indirdik.


cv2.imshow('orj', img)
cv2.imshow('gray', gray)
cv2.imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()