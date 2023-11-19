import cv2
import numpy as np
#kameradan görüntü alma
kamera = cv2.VideoCapture(0)
while True:
    ret,goruntu=kamera.read()            #tek ek görüntü alıcak burda ret ile kontrol edicem

    cv2.imshow("hasan",goruntu)

    if cv2.waitKey(300) & 0xFF ==('q'):
        break

kamera.release()

cv2.destroyAllWindows()