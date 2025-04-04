# f(x, y) = x*a(x'i a yoğunluğunda al) + y*b(y'yi b yoğ al) + c


import cv2
import numpy as np

circle = np.zeros((512,512,3), np.uint8) +255
cv2.circle(circle,(256,256), 60, (255, 0, 0), -1)

rectangle = np.zeros((512,512,3), np.uint8) +255
cv2.rectangle(rectangle, (150,150), (350, 350), (0, 0, 255,), -1)


dst = cv2.addWeighted(circle, 0.6 , rectangle, 0.4, 0)
#p1 = resim  p2 = yoğunluk  p5 = sabit 



cv2.imshow('circle', circle)
cv2.imshow('rectangle', rectangle)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


