# AIPlaylistMaker — Yapılacaklar (To-Do List)

## Kısa Özet
Bu proje, bir çalma listesini analiz edip AI destekli öneriler ve bir sohbet arayüzü sağlayan bir prototip oluşturmayı hedefliyor (Streamlit + Python + ücretsiz/ücretli API entegrasyonları).

---

## İçerik (Kısa)
1. Proje Ortamı ve API Kurulumları
2. Veri Toplama Modülü (Spotify & Genius)
3. Analiz ve AI Öneri Motoru (Gemini Destekli)
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
- [x] `spotipy` ile OAuth kimlik doğrulaması (Kullanıcı Premium Girişi) yapılması ve bağlantının doğrulanması.
- [ ] `spotipy` ile kullanıcıdan alınan playlist linkindeki şarkıların SADECE isim ve sanatçı meta verilerini (Track Name & Artist) çeken fonksiyonun yazılması.
- [ ] `lyricsgenius` ile playlistteki şarkıların sözlerinin metin olarak çekilmesi.

### Kabul Kriterleri
- Playlist'ten şarkı ve sanatçı isimleri (meta veriler) 404/403 hatası almadan başarıyla listelenebiliyor.
- Sözler (lyrics) başarıyla indirilebiliyor veya uygun şekilde mock edilebiliyor.

---

## 3. Analiz ve AI Öneri Motoru (Gemini Destekli)
- [ ] Spotify'dan gelen şarkı listesini Gemini API'ye gönderip şarkıların tahmini teknik verilerini (BPM, Enerji, Enstrümantasyon, 808 sound ağırlığı) **Structured JSON** formatında döndüren Prompt yapısının kurulması.
- [ ] Şarkı sözü metinlerinin Gemini API'ye gönderilerek bağlam (melankolik, hareketli vb.) etiketlerinin çıkarılması.
- [ ] Elde edilen yapay zeka verileriyle playlistin "Profil Vektörü"nün (ortalama BPM, baskın soundlar, söz konsepti) hesaplanması.
- [ ] Gemini API kullanılarak playlist verilerine dayanarak "Bu playlistin konsepti nedir, hangi ruh halinde dinlenir?" açıklama metninin üretilmesi.
- [ ] Belirlenen profile ve konsept etiketlerine uygun yeni şarkı önerilerini (şarkı adı ve sanatçı olarak) doğrudan Gemini'a ürettiren ve bu şarkıları Spotify Search API ile doğrulayan algoritmanın yazılması.

### Kabul Kriterleri
- Gemini API, parça listesini aldığında BPM ve ses tipi içeren geçerli bir JSON çıktısı üretiyor.
- AI konsept açıklaması ve yeni şarkı önerileri tutarlı bir şekilde üretilebiliyor.

---

## 4. Chatbot Modülü Geliştirme
- [ ] Kullanıcıdan gelen serbest metinli promptları (örn. "üzgünüm, 80 bpm keman") işleyip müzikal filtrelere (Düşük valence, Klasik müzik, Akustik) çeviren bir Gemini Prompt Zinciri (Prompt Chain) oluşturulması.
- [ ] Kullanıcının chatbot üzerinden istediği tarza uygun şarkı önerilerini Gemini'a ürettirip, bu şarkıları doğrulamak ve çalma detaylarını almak için Spotify Search API'ye sorgu atan fonksiyonun yazılması.
- [ ] Önerilen şarkının, chatbotun kullanıcıya vereceği doğal ve empati kuran bir cevap metniyle birleştirilmesi.

### Kabul Kriterleri
- Chat prompt → Gemini müzik önerisi akışı çalışıyor ve Spotify Search ile eşleşiyor.
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
- Spotify API artık teknik ses analizlerini (BPM vb.) dışarıya kapattığı için bu verilerin tamamı Gemini API'ye tahmin ettirilecektir.
- LLM'den gelen verilerin kod tarafında kırılma yaratmaması için her zaman `response_format={"type": "json_object"}` veya Pydantic şemaları kullanılmalıdır.
- Gizli anahtarlar `.gitignore` ve `.env` ile korunmalı.

---

## Milestones (Kısa)
- M1: Repo scaffolding + README + basit Streamlit sayfası (1-2 gün)
- M2: Spotify'dan sadece parça listesi çekme + Gemini ile BPM/Sound analizi (2-4 gün)
- M3: Chatbot entegrasyonu + Öneri eşleştirme algoritması (3-5 gün)

---

## Hemen Yapılacaklar / Next Steps
1. Projenin yeni mimarisini içeren `app.py` (Streamlit) iskeletini oluşturmak.
2. `requirements.txt` dosyasını sabitlemek.
3. Spotify'dan bir playlist linki verildiğinde içindeki şarkıların sadece isimlerini temiz bir şekilde çeken fonksiyonu yazmak.