import cv2

img = cv2.imread('resim okuma.png')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #renk uzayı dönüştürme fonksiyonu
#P1= resmin tutulduğu değişken  p2= cv2.colour_(resmin uzayı + 2 + değiştirilmek istene  uzay)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('resim okuma BGR', img)
cv2.imshow('RGB', img_rgb)
cv2.imshow('HSV', img_hsv)
cv2.imshow('GRAY', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


