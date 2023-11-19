import cv2
import numpy as np

kamera = cv2.VideoCapture(0)  #kamerayı bu fonksiyonla başlatıyorum.

while True:
    başarılı,gorüntü = kamera.read()   #kameradan bir görüntü aldım.
    hsv = cv2.cvtColor(gorüntü, cv2.COLOR_BGR2HSV)  #onuda hsv formatına dönüştürdüm.

    lower_red = np.array([0, 100, 100])     #kırmızı renk aralığını belirledim.
    upper_red = np.array([10, 255, 255])

    maske = cv2.inRange(hsv, lower_red, upper_red)   #maskeleme işlemini yaptık  inrange metodu ile
    result = cv2.bitwise_and(gorüntü, gorüntü, maske=maske)  #görüntüyü filtreledik

    cv2.imshow("kamera",gorüntü)
    cv2.imshow('Result', result)    #sonucu ekrana gösterdik.

    if cv2.waitKey(1) & 0xFF == ord('q'):  # çıkışı q ile yaptık
        break

cv2.destroyAllWindows()