import cv2
import numpy as np

image = cv2.imread("pirinc.png")
#gri seviyeye dönüştür.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if image is None:
    print("Resim yüklenemedi. Dosya yolu doğru mu?")
else:
    # işleme devam
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



# Gürültüyü azaltmak için Gauss filtresi uygula
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Eşikleme
_, thresh = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY)

# istenmeyen alanları temizle
kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# Kontur tespiti yap
contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pirinç tanelerini say ve etiketle
rice_count = 0
for contour in contours:
    # Minimum alan kontrolü yaparak gürültüyü azalt
    if cv2.contourArea(contour) > 100:
        # Etiketleme işlemi
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        rice_count += 1

# Sonuçları ekrana yazdır
print("Toplam pirinç sayısı:", rice_count)

# Sonucu göster
cv2.imshow("piric gösterim", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
