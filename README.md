```markdown
# Ki67 Pozitiflik Tespiti

Bu proje, görüntü işleme tekniklerini kullanarak histopatolojik resimlerdeki Ki67 pozitiflik oranını tespit etmek için bir Python scripti sağlar. Proje, Windows ve macOS kullanıcıları için gerekli kurulum adımlarını içerir.
Dikkat QuPath gibi iyi sonuç vermez. Ancak birkaç saniye içinde onlarca resmi inceleyip görşel ve yazı olarak output verir. Arka plan beyaz, 200x veya 400x çekim yapın.
## Özellikler

- JPEG, JPG, PNG formatlarındaki görüntüleri destekler.
- Hücre nükleuslarını analiz eder ve pozitif/negatif oranını hesaplar.
- Analiz edilen görüntülerin üzerine yüzdelik pozitiflik oranını yazar.
- İşlenen görüntüleri ve sonuçları `output` klasörüne kaydeder.

## Gereksinimler

- Python 3.x

## Kurulum

### Windows

1. **Python İndir ve Kur:**

   [Python İndir](https://www.python.org/downloads/) sayfasından Python 3.x sürümünü indirin ve kurun. Kurulum sırasında "Add Python to PATH" seçeneğini işaretlediğinizden emin olun.

2. **Gerekli Kütüphanelerin Kurulumu:**

   Komut istemcisini (Command Prompt) açın ve aşağıdaki komutu çalıştırın:

   ```bash
   pip install opencv-python numpy Pillow
   ```

### macOS

1. **Python İndir ve Kur:**

   macOS'te Python 3.x sürümü genellikle yüklüdür, ancak emin olmak için Terminal'i açın ve şu komutu çalıştırın:

   ```bash
   python3 --version
   ```

   Eğer Python yüklü değilse, [Python İndir](https://www.python.org/downloads/) sayfasından Python 3.x sürümünü indirip kurabilirsiniz.

2. **Gerekli Kütüphanelerin Kurulumu:**

   Terminal'i açın ve aşağıdaki komutu çalıştırın:

   ```bash
   pip3 install opencv-python numpy Pillow
   ```

## Kullanım

1. **Script'i Çalıştırın:**

   Script'in bulunduğu klasöre gidin ve aşağıdaki komutu çalıştırın:

   ```bash
   python3 dogru.py
   ```

   Windows kullanıcıları `python` komutunu kullanabilir:

   ```bash
   python dogru.py
   ```

2. **Sonuçları İnceleyin:**

   Script çalıştıktan sonra `output` klasöründe işlenen görüntüler ve `sonuc.txt` dosyası oluşacaktır. Örnek bir demo görüntüsü ve çıktısı aşağıda verilmiştir:

   - [Demo Görüntü](https://raw.githubusercontent.com/metinciris/ki67/main/demo.jpg)
   - [Demo Çıktısı](https://raw.githubusercontent.com/metinciris/ki67/main/demo_output.jpg)

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
```

### README Dosyasının Özeti:
- **Projenin Amacı:** Ki67 pozitiflik oranını hesaplayan bir Python scripti.
- **Kurulum Talimatları:** Windows ve macOS için Python ve gerekli kütüphanelerin kurulumu.
- **Kullanım:** Script'in nasıl çalıştırılacağı ve sonuçların nasıl görüntüleneceği.
- **Örnek Resimler:** Demo ve demo çıktısı için bağlantılar.
- **Lisans:** Proje MIT Lisansı altında lisanslanmıştır.

Bu dosyayı GitHub reposuna ekleyebilir ve gerektiğinde daha fazla bilgi ekleyebilirsiniz. Eğer eklemek istediğiniz başka bir şey varsa, lütfen bildirin!
