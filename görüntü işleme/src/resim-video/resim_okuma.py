import cv2 
import numpy  
import matplotlib 

img = cv2.imread("resim okuma.png",0)   #imread fonksiyonu resmi okur parametresi=resim adı
#2. prmetr= 0 veya cv2.IMREAD_GRAYSCALE fonksiyonu ile resmi gri tonlarda okutabilriz
# print(img)   #resmin renklerini okudu ve matris olarak yazdırdı

cv2.namedWindow("image",cv2.WINDOW_NORMAL)  #parametre1= pencere adı parametre2=boyutu ayarlamak için gerekli. bu fonk üstte olmalı çünkü burada yerleştirilecek olan pencereyi oluşturuyoruz.
## imshow ve nameWindow bu şekilde altlı üstlü olmalı ve 1.parametreleri aynı olmalı 
cv2.imshow("image", img)  #imshow fonksiyonu= resmi gösterir 1. parametre = resim adı  2. parametre=resmin tutuldupu değişken

cv2.waitKey(0)  #parametreye girilen milisaniye kadar resim açık kalır

cv2.destroyAllWindows()  #genelde her kodun sonuna yazılır.karışıklık önlemek için kullanılır.görevi açık pencereleri kapatmaktır

cv2.imwrite("resim okuma1.png",img)  #kaydeder 1. parametre=oluşturulmak istenen dosyanın adı 2.parmtr=kaydedilecek dosyanın tutulduğu değişken

