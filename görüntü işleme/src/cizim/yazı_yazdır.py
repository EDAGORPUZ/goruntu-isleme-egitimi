import cv2
import numpy as np

canvas = np.zeros((215,515,3), dtype=np.uint8) +255

font1= cv2.FONT_HERSHEY_SIMPLEX
font2= cv2.FONT_HERSHEY_COMPLEX
font3= cv2.FONT_HERSHEY_PLAIN


cv2.putText(canvas, "OPENCV", (40,100), font2, 4, (0,0,0), cv2.LINE_AA )
#p2=metin  p3=metnin başlangıç koordinatı p4=yazı tipi p5=font büyüklüğü  p6=renk  p7=yazı tipi(varsayılan grili)


cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

