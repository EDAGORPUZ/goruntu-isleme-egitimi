import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = np.zeros((500, 500), np.uint8) +50  #siyah tuval oluşturduk
# cv2.rectangle(img, (0, 60), (200, 150), (255, 255, 255), -1)
# cv2.rectangle(img, (200, 150), (350, 300), (255, 255, 255), -1)

img = cv2.imread('smile.jpg')

# cv2.imshow('img', img)

# plt.hist(img.ravel(), 256, [0, 255])#histogram çiz
# #p1= resmi tek bir satır haline getirir  p2= kaç değer var  p3= değer aralığı
# plt.show()#histogramı gör


# b, g, r için ayrı ayrı histogram değerlerini görüyoruz
b, g, r = cv2.split(img)
plt.hist(b.ravel(), 256, [0, 255])
plt.hist(g.ravel(), 256, [0, 255])
plt.hist(r.ravel(), 256, [0, 255])
plt.show()


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
