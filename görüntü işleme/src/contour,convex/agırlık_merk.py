import cv2
import numpy as np

img = cv2.imread("ucgen.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

M = cv2.moments(thresh)
print(M)  #key ve value değerleri tutar


X = int(M['m10']/M['m00']) #ağırlık merkezinin x değeri
Y = int(M['m01']/M['m00'])

cv2.circle(img, (X,Y), 5, (255, 0), -1)



cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
