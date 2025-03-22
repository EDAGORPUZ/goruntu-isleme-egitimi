import cv2

cap = cv2.VideoCapture(0)  #prmtr1= webcam kullanılacak ise 0, bilgisayardan ise videonun adresi


while True:  #videonun uzunluğu bilinmediği için sonsuz döngü oluşturduk.
    
    ret, frame = cap.read()  #fonksiyon kare(frame)leri doğru okuduysa ret değişkeni=true değilse false olacaktır
    frame = cv2.flip(frame,1)  #prmtr2= 1 ise frame y eksenine göre döndürülür 
    cv2.imshow("Webcam", frame)
    
    # cv2.waitKey(30) #her frame ekranda 30 mlsn dönsün(video kalitesini etkiler)
    # #0 yazıldığında ilk frame resim gibi kalır, devam etmez
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  #q tuşuna basıldığında döngüden çık (videoyu kapa)
        break
    
    
cap.release() #video üzerinde işlem yapılabilmesini sağlar(kapatarak)
cv2.destroyAllWindows()

