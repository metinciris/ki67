import cv2
import numpy as np
import os
import winsound

# Görüntüleri analiz eden fonksiyon
def analyze_image(image_path, output_path):
    # Görüntüyü yükle
    img = cv2.imread(image_path)

    # Gürültüyü azaltmak için bulanıklaştırma
    img_blur = cv2.GaussianBlur(img, (3, 3), 0)

    # RGB'den HSV'ye dönüştürme
    hsv_img = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

    # Koyu kahverengi (DAB) nükleer pozitiflik için aralıklar
    lower_dark_brown = np.array([5, 70, 20])
    upper_dark_brown = np.array([20, 255, 200])

    # Açık kahverengi (DAB) nükleer pozitiflik için aralıklar
    lower_light_brown = np.array([10, 30, 10])
    upper_light_brown = np.array([20, 200, 150])

    # Hematoksilen nükleer negatiflik için aralıklar (mavi tonları)
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Koyu kahverengi maske oluşturma
    dark_brown_mask = cv2.inRange(hsv_img, lower_dark_brown, upper_dark_brown)

    # Açık kahverengi maske oluşturma
    light_brown_mask = cv2.inRange(hsv_img, lower_light_brown, upper_light_brown)

    # Mavi (Hematoksilen) maske oluşturma
    blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

    # Morfolojik işlemlerle maske iyileştirme
    kernel = np.ones((5, 5), np.uint8)
    dark_brown_mask = cv2.morphologyEx(dark_brown_mask, cv2.MORPH_CLOSE, kernel)
    light_brown_mask = cv2.morphologyEx(light_brown_mask, cv2.MORPH_CLOSE, kernel)
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, kernel)

    # Küçük gürültüleri filtrelemek için kontur tespiti
    def filter_contours(mask, color):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        filtered_mask = np.zeros_like(mask)
        for cnt in contours:
            if 50 < cv2.contourArea(cnt) < 2000:  # Hücre boyutlarına uygun alan filtresi
                cv2.drawContours(img, [cnt], -1, color, 2)  # Nükleusları işaretle
                cv2.drawContours(filtered_mask, [cnt], -1, 255, -1)
        return filtered_mask, contours

    # Maske ve kontur tespiti
    dark_brown_mask, dark_brown_contours = filter_contours(dark_brown_mask, (0, 0, 255))  # Koyu kahverengi pozitif
    light_brown_mask, light_brown_contours = filter_contours(light_brown_mask, (0, 165, 255))  # Açık kahverengi pozitif
    blue_mask, blue_contours = filter_contours(blue_mask, (255, 0, 0))  # Negatif hücreler

    # Hücre sayımı
    total_nuclei = len(dark_brown_contours) + len(light_brown_contours) + len(blue_contours)
    positive_nuclei = len(dark_brown_contours) + len(light_brown_contours)
    negative_nuclei = len(blue_contours)

    # Pozitiflik yüzdesini hesapla
    if total_nuclei > 0:
        positive_percentage = (positive_nuclei / total_nuclei) * 100
    else:
        positive_percentage = 0

    # Pozitiflik yüzdesini resmin bir köşesine yazma
    cv2.putText(img, f"%{positive_percentage:.2f} pozitif", (10, img.shape[0] - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # İşlenen resmi kaydet
    cv2.imwrite(output_path, img)

    return total_nuclei, positive_nuclei, negative_nuclei

# Ana işleme fonksiyonu
def process_images():
    # Python dosyasının bulunduğu klasör
    input_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(input_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    results = []

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            total_nuclei, positive_nuclei, negative_nuclei = analyze_image(input_path, output_path)
            positive_percentage = (positive_nuclei / total_nuclei) * 100 if total_nuclei > 0 else 0

            results.append(f"{filename} %{positive_percentage:.2f} pozitif.\nPozitif: {positive_nuclei}\nNegatif: {negative_nuclei}\n")

    # Sonuçları bir txt dosyasına yazma
    results_path = os.path.join(output_dir, 'sonuc.txt')
    with open(results_path, 'w') as f:
        f.writelines(results)

    return results_path

# Resimleri işleme
results_path = process_images()

# İşlem tamamlandığında bildirim
print(f"Hücre tespiti tamamlandı ve sonuçlar {results_path} dosyasına kaydedildi.")

# Beep sesi çal
winsound.Beep(1000, 500)  # 1000 Hz frekansta, 500 ms süresinde beep sesi
