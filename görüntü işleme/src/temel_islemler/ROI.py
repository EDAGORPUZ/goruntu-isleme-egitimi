#ROI = ilgi alanı(resimdeki kişinin gözlerinin açıklığını tespit etmek istiyorsak sadece göz bölgesini işlemek)
import cv2

img = cv2.imread("resim okuma.png")
print(img.shape[:2])

roi = img[30:200, 230:400]  #p1= boydan 30-200 arasını p2= enden 230,400 arasını tara
cv2.imshow('roi', roi)


cv2.imshow('resim_okuma', img)
cv2.waitKey(0)
cv2.destroyAllWindows()







