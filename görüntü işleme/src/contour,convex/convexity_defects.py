import cv2
import numpy as np

img = cv2.imread('star.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)

contours, ret = cv2.findContours(thresh, 2, 1)

cnt = contours[0]

hull = cv2.convexHull(contours[0], returnPoints= False) #false= değerlerin kendisini değil indislerini döndürür.

defects = cv2.convexityDefects(contours[0], hull)


for i in range(defects.shape[0]):  #defects in 0. elemanı kadar i dönsün
    s, e, f, d = defects[i, 0]
    #s=start  e=end  f= en uzak nokt  d=mesafe
    
    strat = tuple(cnt[s][0]) #baş noktası
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, strat, end, [0, 255, 0], 2)
    cv2.circle(img, far, 5, [0, 255, 0], -1)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



