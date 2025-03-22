import cv2
import numpy as np

img = np.zeros((10,10,3), np.uint8)  #boyutlar küçük old için resize ile yenide boyutlandıracağız.
# zeros fonks 3.parmtresinin 3 olması renkler üzerinde çalıştığımızı gösterir.
#3 ü silersek gri tonlarında çalışırız
#pixel boyama
img[0,0] = (255, 255, 255) 
img[0,1] = (255, 255, 200)
img[0,2] = (255, 255, 150)
img[0,3] = (255, 255, 15)

img = cv2.resize(img, (900,500), interpolation=cv2.INTER_AREA)

cv2.imshow("Canvas", img)
cv2.waitKey(0)
cv2.destroyAllWindows


#gri tonlar

img2 = np.zeros((10,10), np.uint8)

img2[0,0] = (255) 
img2[0,1] = (200)
img2[0,2] = (150) 
img2[0,3] = 15


img2 = cv2.resize(img2, (900,500), interpolation=cv2.INTER_AREA)

cv2.imshow("Canvas", img2)
cv2.waitKey(0)
cv2.destroyAllWindows


