import cv2


img = cv2.imread("resim okuma.png")

cv2.namedWindow("resim okuma.png",cv2.WINDOW_NORMAL)  #parametre1= pencere adı parametre2=boyutu ayarlamak için gerekli. 
#bu fonk üstte olmalı çünkü burada yerleştirilecek olan pencereyi oluşturuyoruz.
## imshow ve nameWindow bu şekilde altlı üstlü olmalı ve 1.parametreleri aynı olmalı 
cv2.imshow("resim okuma.png", img)  #imshow fonksiyonu= resmi gösterir 1. parametre = resim adı  2. parametre=resmin tutuldupu değişken

img = cv2.resize(img,(640,480))  #resim bu boyutlarda oluşacak


cv2.waitKey(0)
cv2.destroyAllWindows()
