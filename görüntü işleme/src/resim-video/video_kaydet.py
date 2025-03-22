import cv2

cap = cv2.VideoCapture(0)

fileName = r'C:\Users\Eda\Desktop\görüntü işleme\webcam.avi'   #video bu dosya içine webcam.avi şeklinde kaydedilecek
codec = cv2.VideoWriter_fourcc('W','M','V','2') #videodaki verileri 4 karakter ile tanımlar değerlere fourcc.org sitesinden bakabilirsin.
frameRate = 30  #(frame alanı)
resolution = (640, 480)  #(çözünürlük)
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)


while True:
    ret, frame = cap.read()
    videoFileOutput.write(frame) #frameleri kaydedilecek değişkenin içine yaz.
    
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()


#fileName = r'C:\Users\Eda\Desktop\görüntü işleme\webcam.avi'  eğik çizgi ve harf ikilisini komut olarak kabul ettiği için
# r kullanarak bu sorunu düzelttik.

