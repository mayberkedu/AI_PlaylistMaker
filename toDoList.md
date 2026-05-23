# AIPlaylistMaker — Yapılacaklar (To-Do List)

## Kısa Özet
Bu proje, bir çalma listesini analiz edip AI destekli öneriler ve bir sohbet arayüzü sağlayan bir prototip oluşturmayı hedefliyor (Streamlit + Python + ücretsiz/ücretli API entegrasyonları).

---

## İçerik (Kısa)
1. Proje Ortamı ve API Kurulumları
2. Veri Toplama Modülü (Spotify & Genius)
3. Analiz ve AI Öneri Motoru
4. Chatbot Modülü Geliştirme
5. Streamlit ile Web Arayüzü (Frontend)

---

## 1. Proje Ortamı ve API Kurulumları
- [x] Python sanal ortamı (virtual environment) oluşturulması.
- [x] Gerekli kütüphanelerin kurulması (örnek: streamlit, spotipy, lyricsgenius, google-generativeai, python-dotenv).
- [x] Spotify Developer, Genius ve Google AI Studio (Gemini) platformlarından API anahtarlarının alınması (Hazırlığı yapıldı, kullanıcı .env dosyasına ekleyecek).
- [x] API anahtarlarının projede güvenli kullanımı için `.env` dosyasına eklenmesi ve `.env.example` oluşturulması.

### Kabul Kriterleri
- Sanal ortam hazır ve `requirements.txt` veya `pyproject.toml` ile bağımlılıklar listelenmiş.
- `.env.example` mevcut, gizli anahtarlar repo'ya eklenmemiş.

---

## 2. Veri Toplama Modülü (Spotify & Genius)
- [ ] `spotipy` ile kullanıcıdan alınan playlist linkindeki şarkıların listesini çeken fonksiyonun yazılması.
- [ ] Audio Features endpoint'i kullanılarak şarkıların BPM, enerji, valence (duygu durumu) verilerinin çekilmesi.
- [ ] Şarkıların tür (genre) ve akustik/elektronik oranlarının analiz edilerek ses profillerinin (örn. alt frekans/bass karakteristiği) belirlenmesi.
- [ ] `lyricsgenius` ile playlistteki şarkıların sözlerinin metin olarak çekilmesi.

### Kabul Kriterleri
- Playlist'ten şarkı meta verileri ve audio-feature verileri alınabiliyor.
- Sözler (lyrics) başarıyla indirilebiliyor veya uygun şekilde mock edilebiliyor.

---

## 3. Analiz ve AI Öneri Motoru
- [ ] Çekilen verilerle playlistin matematiksel "Profil Vektörü"nün (ortalama BPM, enerji seviyesi vb.) hesaplanması.
- [ ] Şarkı sözü metinlerinin Gemini API'ye (veya seçilecek LLM'ye) gönderilerek bağlam (melankolik, hareketli vb.) etiketlerinin çıkarılması.
- [ ] Gemini (veya seçilecek model) kullanılarak, analiz edilen playlist verilerine dayanarak "Bu playlistin konsepti nedir?" sorusunun AI tarafından açıklanması.
- [ ] Belirlenen profile ve konsept etiketlerine uygun yeni şarkıların Spotify'da aranmasını sağlayan öneri algoritmasının yazılması.

### Kabul Kriterleri
- Profil vektörü hesaplama modülü çalışıyor ve bir örnek giriş için beklenen özet değerleri üretiyor.
- AI etiketlemesi tutarlı ve örnek çıktılarla doğrulanabiliyor.

---

## 4. Chatbot Modülü Geliştirme
- [ ] Kullanıcıdan gelen serbest metinli promptları (örn. "üzgünüm, 80 bpm keman") işleyip Spotify'ın anlayacağı parametrelere (düşük valence, 80 tempo, akustik) çeviren bir prompt zinciri (Prompt Chain) oluşturulması.
- [ ] Çıkarılan parametrelerle Spotify Search API'ye sorgu atan fonksiyonun yazılması.
- [ ] Önerilen şarkının, chatbotun kullanıcıya vereceği doğal ve empati kuran bir cevap metniyle birleştirilmesi.

### Kabul Kriterleri
- Chat prompt → parametre dönüşümü çalışıyor ve örnek sorgularla doğrulanabiliyor.
- Chatbot önerisi kullanıcıya okunaklı bir metin olarak dönüyor.

---

## 5. Streamlit ile Web Arayüzü (Frontend)
- [ ] `st.set_page_config` ile ana sayfa yapısının ve başlıkların ayarlanması.
- [ ] Sayfanın `st.tabs` ile iki ana sekmeye ayrılması: "Playlist Analizi" ve "AI Chatbot".
- [ ] 1. Sekme: Playlist linki almak için `st.text_input` alanı eklenmesi ve işlemler sürerken `st.spinner` ile yükleme animasyonu gösterilmesi.
- [ ] AI tarafından üretilen playlist açıklamasının ve önerilen şarkıların listesinin arayüzde görselleştirilmesi (örn. `st.dataframe` veya özel kartlar).
- [ ] 2. Sekme: Streamlit'in `st.chat_message` ve `st.chat_input` bileşenleri ile chatbot arayüzünün oluşturulması.
- [ ] Chat geçmişinin silinmemesi için oturum durumu (`st.session_state`) yapılandırılması.

### Kabul Kriterleri
- Streamlit arayüzü çalışır durumda ve temel akışları sergileyebiliyor (analiz + chatbot).

---

## Ek Notlar / İyi Uygulamalar
- Önce mock veri ve fonksiyonlarla başlayın; API anahtarlarını sonradan ekleyin.
- Küçük, test edilebilir parçalar halinde ilerleyin (örn. önce profil vektörü, sonra lyrics etiketleme, vs.).
- Gizli anahtarlar `.gitignore` ve `.env` ile korunmalı.

---

## Milestones (Kısa)
- M1: Repo scaffolding + README + basit Streamlit sayfası (1-2 gün)
- M2: Veri toplama + profil hesaplama + AI etiketleme (2-5 gün)
- M3: Chatbot + öneri algoritması + export seçenekleri (sonraki hafta)

---

## Hemen Yapılacaklar / Next Steps
1. Projenin runtime'ını (Python) onayla ve bir `README.md` ile temel çalıştırma talimatlarını ekle.
2. `requirements.txt` oluştur (ilk sürüm: streamlit, spotipy, lyricsgenius, python-dotenv).
3. Basit bir `app.py` (Streamlit) iskeleti ekleyip çalıştır (örnek: `streamlit run app.py`).

---

Dosya güncellendi: biçim düzenlendi ve görevler daha okunabilir hale getirildi. İstersen şimdi `README.md`, `requirements.txt` ve bir minimal `app.py` iskeleti oluşturabilirim.
