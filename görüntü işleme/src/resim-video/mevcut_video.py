import cv2

cap = cv2.VideoCapture("fizik.mp4")

while True:
    ret, frame =cap.read()
    if ret == 0:   #video bittiğinde pencereyi kapa
        break
    
    frame = cv2.flip(frame,1)
    
    cv2.imshow("fizik.mp4", frame)
    
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()


