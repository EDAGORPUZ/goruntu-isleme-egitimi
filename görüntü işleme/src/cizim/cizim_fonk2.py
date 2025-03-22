import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) +255

#line fonk = çizgi çizer
cv2.line(canvas, (50,50), (512,512), (255,0,0), thickness=5)
#p1=tuval adı  p2=baş nokt  p3=bit nokt  p4=renk  p5=kalınlık

cv2.line(canvas, (100,50), (200,250), (0,0,255), thickness=7)


#rectangle fonk = dikdörtgen çizer
cv2.rectangle(canvas, (20,20), (50,50), (0,255,0), thickness=3)
#p1=tuval adı  p2=sol üst köşe  p3=sağ alt köşe  p4=renk  p5=kalınlık
#kalınlık yerine -1 girersek dikdörtgenin içi dolu olur


#circle fonk = çember çizer
cv2.circle(canvas, (250,250), 100, (0,0,255), thickness=10)
#p1=tuval adı  p2=merkes nokt  p3=yarıçap  p4=renk  p5= kalınlık


#3 ayrı çizgi ile üçgen çizimi
p1 = (100,400)
p2 = (70,70)
p3 = (300,300)

cv2.line(canvas, p1, p2, (0,0,0), 4)  #p1den p2ye çizgi çiz
cv2.line(canvas, p2, p3, (0,0,0), 4)
cv2.line(canvas, p3, p1, (0,0,0), 4)

#poliline fonk = farklı düzgün geometrik şekiller
points = np.array([[[55,60],[463,169],[330,200],[220,260]]], np.int32) 

cv2.polylines(canvas, [points], True, (0,0,100),5 )
#p2=noktalar p3=kapalı şekil için p4=renk p5=kalınlık


#ellipse fonk = elips 

cv2.ellipse(canvas, (255,255), (80,30), 10 , 55, 360, (260,280,0), -1)
#p2=merkez  p3=en,boy  p4=yatayla yapacağı açı  p5= başlangıç ve bitiş açısı  p6=renk p7=kalınlık


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()




