import cv2
import numpy as np

cap = cv2.VideoCapture('dog.mp4')

while 1:
    ret, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #HSV'ye çevirdik çünkü bu şekilde nesne takibi daha kolay
    
    sensivity = 15
    lower_white = np.array([0, 0, 255 - sensivity])
    upper_white = np.array([255, sensivity, 255])
    #hsv için aralık belirledik
    
    mask = cv2.inRange(hsv, lower_white, upper_white)
    #lower_white ve upper_white araasındaki değerlere maske uygula ve kalan değerleri sil
    
    res = cv2.bitwise_and(frame, frame, mask = mask)
    #maskın doğru uygulanabilmesi için yazdık
    
    cv2.imshow('frame', frame)
    cv2.imshow('maask', mask)
    cv2.imshow('result', res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()



