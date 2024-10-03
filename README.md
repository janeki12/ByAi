# ByAi Roadmap

## Öne Çıkan Özellikler:

1. **Konu Belirleme:** Kullanıcılar, istedikleri herhangi bir konuda içerik oluşturabilecekler.
2. **Araştırma:** Program, interneti tarayarak en güncel ve doğru bilgileri toplayacak.
3. **Hikaye Akışı:** Toplanan bilgiler, akıcı bir sunum formatında düzenlenecek.
4. **Seslendirme:** İçerik, yapay zeka tarafından seslendirilecek.
5. **Otomatik Video Üretimi:** Video düzenleme süreci tamamen otomatikleştirilecek.
6. **YouTube Entegrasyonu:** Oluşturulan videolar, doğrudan YouTube'a yüklenecek.

Bu proje, video üretim sürecini daha hızlı, erişilebilir ve verimli hale getirmeyi amaçlamaktadır.

## Kullanıcı Arayüzü Özellikleri:

1. **Kanal Oluşturma:** Kullanıcıya "Kaç adet YouTube kanalı oluşturmak istersiniz?" sorusu yöneltilir. Kullanıcı istediği sayıda kanal oluşturabilir.
2. **Kanal Türü Seçimi:** Kullanıcı her kanal için içerik türünü belirleyebilir. Seçenekler şunlardır:
   - Eğitim
   - Belgesel
   - Eğlence
   - Oyun
   - Seyahat
   - Teknoloji
   - Yemek tarifleri
   - Diğer (kullanıcı tanımlar)
3. **Özelleştirme:** Her kanal için isim, açıklama ve profil resmi gibi bilgiler düzenlenebilir.
4. **Tema ve Tasarım:** Kullanıcılar, kanalları için çeşitli şablonlar ve renk paletlerinden seçim yapabilir.
5. **Eğitim Modülü:** Kullanıcılar, içerik üretim sürecine dair eğitim modüllerine erişebilir.

## Detaylandırılmış Süreç

Bu projede videoların otomatik üretim süreci aşağıdaki adımlar halinde çalışacaktır:

### 1. **Metin Dosyası Oluşturma:**
   - Program, internette araştırma yaparak kullanıcı tarafından belirlenen konuda bilgileri toplar.
   - Bu metinler **`/data/text/`** klasörüne kaydedilir.
   - Örnek: `"konu_belirleme_metni.txt"` dosyasına yazılır.

### 2. **Metni Parçalara Ayırma:**
   - Kaydedilen metinler, belirlenen bir Python betiği (örneğin: **`text_splitter.py`**) ile satırlara ayrılır.
   - Her satır, görsel haline getirilir ve **`/output/images/`** klasörüne **`gorsel_<satir_no>.png`** formatında kaydedilir.
   - Bu işlem için kullanılacak betik: **`text_to_image.py`**.

### 3. **Ses Dosyası Üretimi:**
   - Ayrılan metinler, yapay zeka seslendirme teknolojisi kullanılarak ses dosyasına dönüştürülür.
   - Ses dosyaları **`/output/audio/`** klasörüne **`seslendirme_<satir_no>.mp3`** olarak kaydedilir.
   - Ses dosyasını oluşturmak için betik: **`text_to_speech.py`**.

### 4. **Videonun Oluşturulması:**
   - Görseller ve ses dosyaları, video düzenleme yazılımı (örneğin, **`video_creator.py`**) tarafından birleştirilir.
   - Hafif bir arka plan müziği eklenir.
   - Videolar, **`/output/videos/`** klasörüne **`final_video.mp4`** olarak kaydedilir.

### 5. **YouTube'a Yükleme:**
   - Kullanıcı bilgileri, veritabanından alınarak doğrulanır (**`user_db.py`**).
   - Hazırlanan video, kullanıcının YouTube hesabına API aracılığıyla yüklenir.
   - Yükleme işlemi **`youtube_uploader.py`** betiği tarafından yapılır.

### 6. **Süre Hesaplama:**
   - Bir videonun oluşturulması ve YouTube'a yüklenmesi ortalama **2 dakika** sürmektedir.
   - Bu süreçler, video uzunluğuna, içerik detayına ve internet hızına bağlı olarak değişiklik gösterebilir.

## Özet

- Kullanıcı, bir konuda içerik belirler ve başlatır.
- Metinler yazılır, görseller ve ses dosyaları oluşturulur.
- Videolar, müzikle birlikte birleştirilir ve YouTube'a yüklenir.
- Tüm bu işlemler 2 dakika içinde tamamlanacak şekilde optimize edilmiştir.
