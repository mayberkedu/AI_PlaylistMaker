# Tamamlanan Görevler (Finished Tasks)

Bu dosya, projede tamamlanan görevlerin teknik detaylarını ve nasıl çalıştığını belgelemek için tutulmaktadır.

## 1. Proje Ortamı ve API Kurulumları

**Durum:** Tamamlandı
**Tarih:** 23 Mayıs 2026

**Yapılanlar ve Çalışma Mekanizması:**
- **Sanal Ortam (Virtual Environment):** Proje bağımlılıklarını izole etmek için `python -m venv venv` komutu ile bir sanal ortam oluşturuldu. Bu, işletim sistemindeki diğer Python projeleriyle çakışmaları önler.
- **Bağımlılıklar (`requirements.txt`):** Proje için kullanılacak temel kütüphaneler (`streamlit`, `spotipy`, `lyricsgenius`, `google-generativeai`, `python-dotenv`) belirlendi ve `requirements.txt` dosyasına eklendi.
- **Güvenlik ve Çevresel Değişkenler (`.env.example` & `.env`):** API anahtarlarının kod içerisinde açıkça bulunmaması (hardcode edilmemesi) ve Git repo'suna yanlışlıkla gönderilmemesi için çevresel değişken (environment variables) yapısı kuruldu. `python-dotenv` paketi bu değişkenleri kod içerisine yükleyecek.
- **Versiyon Kontrol (`.gitignore`):** Sanal ortam dosyaları (`venv/`), hassas veriler (`.env`) ve Python önbellek dosyaları Git tarafında yoksayılacak şekilde yapılandırıldı.

_Not: API anahtarlarınızı oluşturduktan sonra projedeki `.env` dosyasını düzenleyerek yerleştirmeniz gerekmektedir._
