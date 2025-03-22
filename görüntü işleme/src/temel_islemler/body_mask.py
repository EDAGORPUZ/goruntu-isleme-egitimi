import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('trackbar')
cv2.resizeWindow('trackbar', 500, 500)

#alt ve üst değerler için trackbar oluşturduk
cv2.createTrackbar('lower H', 'trackbar', 0, 180, nothing)
cv2.createTrackbar('lower S', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('lower V', 'trackbar', 0, 255, nothing)

cv2.createTrackbar('upper H', 'trackbar', 0, 180, nothing)
cv2.createTrackbar('upper S', 'trackbar', 0, 255, nothing)
cv2.createTrackbar('upper V', 'trackbar', 0, 255, nothing)

#üst değerlerin max değerde durması sağlanır
cv2.setTrackbarPos('upper H', 'trackbar', 180)
#p1=kızak adı  p2=pencere adı  p3=durması istenen değer
cv2.setTrackbarPos('upper S', 'trackbar', 255)
cv2.setTrackbarPos('upper V', 'trackbar', 255)


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerH = cv2.getTrackbarPos('lower H', 'trackbar')
    lowerS = cv2.getTrackbarPos('lower S', 'trackbar')
    lowerV = cv2.getTrackbarPos('lower V', 'trackbar')
    
    upperH = cv2.getTrackbarPos('upper H', 'trackbar')
    upperS = cv2.getTrackbarPos('upper S', 'trackbar')
    upperV = cv2.getTrackbarPos('upper V', 'trackbar')
    
    #değişkenleri dizi içinde saklıyoruz
    lower_color = np.array([lowerH, lowerS, lowerV])
    upper_color = np.array([upperH, upperS, upperV])
    
    mask = cv2.inRange(frame_HSV, lower_color, upper_color)
    
    
    cv2.imshow('ooriginal', frame)
    cv2.imshow('mask', mask)
    
    
    if cv2.waitKey(20) & 0xFF ==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()









