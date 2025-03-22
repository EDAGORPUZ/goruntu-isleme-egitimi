import cv2
import numpy as np

img = cv2.imread('helikopter.png', 0)


# işlemlerin tamamnına kılavuzdan bakabilrisin 

kernel = np.ones((5,5), np.uint8)
#kernel= matris değeri

erosion = cv2.erode(img, kernel, iterations= 1)
#iterations= tekrar etme sayısı

dilation = cv2.dilate(img, kernel, iterations=1)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)
#gürültü siler

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE,kernel)
#resmin içindeki uyyumsuzluklar giderilir

cv2.imshow('dilation', dilation)
cv2.imshow('original', img)
cv2.imshow('erosion', erosion)
cv2.imshow('opening', opening)
cv2.imshow('closing', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()




