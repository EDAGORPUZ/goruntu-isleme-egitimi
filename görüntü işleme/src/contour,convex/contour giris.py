#convex hull = içbükey şekillere dışbükey örtü çizmek
#convexity defects = dışbükey kusur(örtüden sapılan yer) 

import cv2
img = cv2.imread('contour1.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, tresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#bu fonks 3 değer döndürüyor 1 ve 3. değerler kullanılmayacak. Son 2 prmtre varsayılandır.

#print(contours)   kontür koordinatlarını yazdırır

cv2.drawContours(img, contours, -1, (0, 0, 255),3)
#p1=işlem yapılacak resim  p2=koordinatlar  p4=renk  p5=kalınlık


cv2.imshow('contour', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



 