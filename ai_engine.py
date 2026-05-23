import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from data_collection import verify_track_on_spotify

# Çevresel değişkenleri yükle
load_dotenv()

# Gemini API yapılandırması
gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    print("Uyarı: GEMINI_API_KEY .env dosyasında bulunamadı.")
else:
    genai.configure(api_key=gemini_api_key)

# Modeli başlat (Gemini 2.0 Flash veya Pro tercih edilebilir genel kullanım için flash hızlıdır)
# JSON formatında temiz dönüş alabilmek için generation_config kullanılabilir.
MODEL_NAME = "gemini-flash-latest"

def analyze_playlist_with_gemini(tracks_data):
    """
    Spotify'dan çekilen parça listesini Gemini'a gönderip,
    tahmini BPM, Enerji, konsept ve ruh halini JSON olarak döndürür.
    """
    if not gemini_api_key:
        return {"error": "Gemini API anahtarı eksik."}

    try:
        model = genai.GenerativeModel(MODEL_NAME)

        # Parçaları metin olarak formatla
        tracks_text = "\n".join([f"- {t['track_name']} (Sanatçı: {t['artist']})" for t in tracks_data])

        prompt = f"""
Aşağıda bir kullanıcının Spotify çalma listesindeki şarkılar verilmiştir. 
Bu şarkıları müzikal olarak analiz etmeni ve aşağıdaki bilgileri bana SADECE GEÇERLİ BİR JSON formatında döndürmeni istiyorum.
Verilen şarkıların türlerini, genel temposunu ve hissiyatını tahmin et.

Şarkı Listesi:
{tracks_text}

Lütfen dönen JSON verisi tam olarak aşağıdaki yapıya sahip olsun:
{{
  "playlist_concept": "Çalma listesinin genel konsepti (kısa bir cümle)",
  "mood": "Dinleme ruh hali (melankolik, enerjik, odaklanma vb.)",
  "average_bpm": "Tahmini ortalama BPM (Sayısal değer veya aralık)",
  "dominant_genres": ["Tür 1", "Tür 2"],
  "musical_profile": "Enstrümantasyon, vokaller, 808 ağırlığı vb. hakkında kısa bir özet"
}}
"""
        # Gemini 1.5 modelleri json çıktısını destekler
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"
            )
        )

        # Yanıtı JSON'a çevir
        result_json = json.loads(response.text)
        return result_json

    except Exception as e:
        print(f"Gemini API Playlist Analiz Hatası: {e}")
        return {"error": str(e)}

def analyze_lyrics_with_gemini(lyrics_text):
    """
    Şarkı sözlerini analiz ederek ana temaları ve duyguları çıkarır.
    """
    if not gemini_api_key or not lyrics_text:
        return None

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = f"""
Aşağıdaki şarkı sözlerini analiz et ve ana temasını, hissettirdiği duyguyu çıkar. SADECE GEÇERLİ BİR JSON formatında yanıt ver.

Şarkı Sözleri:
{lyrics_text[:1500]}... (Sözlerin bir kısmı)

Beklenen JSON Yapısı:
{{
  "theme": "Ana Tema (Aşk, İhanet, İsyan, Umut vb.)",
  "emotion": "Baskın Duygu",
  "summary": "Sözlerin ne anlattığına dair 1-2 cümlelik kısa özet"
}}
"""
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Gemini API Söz Analiz Hatası: {e}")
        return None

def get_recommendations_with_gemini(profile_data, count=5):
    """
    Playlist profiline dayanarak yeni şarkı önerilerinde bulunur.
    """
    if not gemini_api_key or "error" in profile_data:
        return []

    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = f"""
Bana aşağıdaki müzik profiline mükemmel şekilde uyacak {count} adet yeni şarkı önerisinde bulun. 

Profil:
- Konsept: {profile_data.get('playlist_concept')}
- Ruh Hali: {profile_data.get('mood')}
- Ortalama BPM: {profile_data.get('average_bpm')}
- Türler: {', '.join(profile_data.get('dominant_genres', []))}
- Müzikal Profil: {profile_data.get('musical_profile')}

Lütfen cevabını SADECE GEÇERLİ BİR JSON listesi (array) formatında ver. 
Her bir eleman şu yapıda olmalı:
[
  {{
    "track_name": "Şarkı Adı",
    "artist": "Sanatçı Adı",
    "reason": "Bu listeye neden uyduğu hakkında 1 cümle"
  }}
]
"""
        response = model.generate_content(
            prompt,
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json"
            )
        )
        recommendations = json.loads(response.text)

        verified_recs = []
        for rec in recommendations:
            track_name = rec.get("track_name")
            artist = rec.get("artist")
            if track_name and artist:
                verification = verify_track_on_spotify(track_name, artist)
                if verification:
                    rec["spotify_url"] = verification["spotify_url"]
                    rec["album_cover"] = verification["album_cover"]
                    verified_recs.append(rec)
                else:
                    print(f"Doğrulanamadı, listeden çıkarıldı: {track_name} - {artist}")
        
        return verified_recs
    except Exception as e:
        print(f"Gemini API Öneri Hatası: {e}")
        return []
