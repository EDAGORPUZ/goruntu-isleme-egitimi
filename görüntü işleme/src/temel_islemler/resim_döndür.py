import cv2
import numpy as np

img = cv2.imread('ART.JPG')

#DÜZGÜN BİR YENİDEN BOYUTLNDIRMA YAPTIM ÖNEMLİ!!!!!!!!!
row, col = img.shape[:2]
row = 600
col = 400
n_img = cv2.resize(img, (row, col))

M = cv2.getRotationMatrix2D((col/2, row/2), 90, 0.5)
#2 boyutta rotasyon uygulanacak p1=sütun p2= satır p3=yön p4=ölçek

dst = cv2.warpAffine(n_img, M, (col, row))


cv2.imshow('dst', dst)
cv2.imwrite('ART.JPG', n_img)
cv2.imshow('original', n_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

