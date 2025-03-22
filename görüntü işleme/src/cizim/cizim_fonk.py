import cv2
import numpy as np

canvas = np.zeros((512,512,3), dtype=np.uint8) + 255 #parametre boyurlarında siyah tuval oluşturur
#np.uint8=çizim için kullanılan veri tipi   +255 ile matris toplaması yaptık 0+255=255 oldu yani tuval beyaza döndü.
print(canvas)  #0lardan oluşan matris çıktısı aldık 0= siyah

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()






