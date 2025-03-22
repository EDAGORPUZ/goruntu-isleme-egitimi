import cv2
import numpy as np

cap = cv2.VideoCapture(0) #varsayılan kamerayı açtık

while True:     #kameradan gelen frameler okundu ve frame değişkenine atandı
    ret, frame = cap.read()
    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):   #q tuşuna kapatma işlemi ile aynı şablon sadece if'in altında kaydet fonksiyonu kulandık.
        cv2.imwrite('savedframe.jpg', frame)
        break
    
    
cap.release()
cv2.destroyAllWindows()

