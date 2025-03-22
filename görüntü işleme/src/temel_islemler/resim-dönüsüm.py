import cv2
import numpy as np

img = cv2.imread('ART.JPG',0)

#resmi yeniden boyutlandırdım ve bu boyutları değişkenlere atadım.
cv2.namedWindow('ART.JPG', cv2.WINDOW_NORMAL)
new_size=(500, 600)
resized_img = cv2.resize(img, new_size)
row, col = resized_img.shape[:2]

print(row, col)


M = np.float32([[1, 0, 100], [0, 1, 55]]) #[1, 0, yatay açıklık], [0, 1, dikey açıklık]

dst = cv2.warpAffine(img, M, (col, row))
#M matrisinde yapılan işlemi dst içinde tutuyoruz. (önce sütun sonra satır yazılıyor dikkat)



cv2.imshow('dst', dst)
cv2.imshow('ART.JPG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

