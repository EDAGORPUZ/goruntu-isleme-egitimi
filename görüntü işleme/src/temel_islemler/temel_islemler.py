import cv2
import numpy as np

img = cv2.imread("resim okuma.png")

dimention = img.shape   #resmin boyutlarını yazdırır.
print(dimention)   

color = img[150, 200]   #150,200 deki pixelin bgr değerleri tutulur
print('BGR: ', color)  #[blue,green,red]

blue = img[250, 130, 0]  #[p3= blue değeri için(kırmızıyı yazdırmak isteseydik 2 yazardık)]
print('blue: ' , blue)

img[250, 130, 0] = 250   #pixelin b değerini değiştirerek 250 olarak tanımladık
print('new blue :', img[250, 130, 0] )

blue1 = img.item(150, 200, 0) #150,200 pixelindeki mavi rengi blue1 içinde tutuyoruz
print('blue1: ', blue1)
new_blue1 = img.itemset((150, 200, 0), 172) #p1=150,200 pixelindeki mavi değeri p2=yeni belirlenen renk nmarası
print('new blue1: ', img[150, 200, 0])


cv2.imshow("resim okuma", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


