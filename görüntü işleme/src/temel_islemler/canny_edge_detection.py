#cv2.Canny(imput, min treshold, max treshold)

import cv2

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    edges = cv2.Canny(frame, 100, 200)
    #framelerde köşee bulunmuş görüntü burada depolanır.
    
    cv2.imshow('original', frame)
    cv2.imshow('edges', edges)
    
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()




