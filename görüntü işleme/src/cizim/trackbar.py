import cv2
import numpy as np

def nothing(x):
    pass

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')  #trackbar arayüzünü bu pencereye yerleştireceğimiz  için pencreye isim verdik

cv2.createTrackbar("R", "image", 0, 255, nothing)
#p1= kızağın adı kırmızı için R girdik  p2=kızağın yerleşeceği pencere adı
#p3,p4= kızağın başlangıç ve bitiş değerleri (rgb değerleri zaten 0-255 aralığında)  p5= boş fonk
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)

switch = "0 : OFF, 1 : ON"  #(anahtar oluşturduk)
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True:               #pencerenin kapanmaması için sonsuz döngü
    cv2.imshow('image', img)   #image penceresinde img değşkeni için
    if cv2.waitKey(1) & 0xFF == ord('q'):   #1 mlsn'de pencere yenilensin ve q'ya basıldığında kapansın.
        break
    
    r = cv2.getTrackbarPos("R", "image")  #değerleri aldık
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos(switch, "image")
    
    if s == 0:
        img[:] = [0, 0, 0]
        
    else:
        img[:] = [b, g, r] #img'nin tüm pixel değerleri alınan b,g,r değerlerine eşitlensn
        

    
cv2.destroyAllWindows()





