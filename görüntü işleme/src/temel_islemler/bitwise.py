import cv2
import numpy as np


img1 = cv2.imread('bitwise_1.png')
img2 = cv2.imread('bitwise_2.png')

bit_and = cv2.bitwise_and(img1, img2)
#siyah= 0, beyaz= 1 olarak baz alınır, ve bağlacına göre matematiksel işlem yapılır

bit_or = cv2.bitwise_or(img1, img2)
#veya bağlacına göre işlem yapılır.

bit_xor = cv2.bitwise_xor(img1, img2)
#1 ve 1 karşılaşınca= 0  diğer tüm durumlar = 1

bit_not1 = cv2.bitwise_not(img1)
#terse çevirir

cv2.imshow('not1', bit_not1)
cv2.imshow('original1', img1)
cv2.imshow('original2', img2)
cv2.imshow('bit_and', bit_and)
cv2.imshow('bit_or', bit_or)
cv2.imshow('bit_xor', bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()




