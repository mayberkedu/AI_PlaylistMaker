import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# API anahtarlarını yükle
load_dotenv()

# Spotify'a bağlan
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-private"
))


def test_api_connection():
    print("\n⏳ Spotify API Bağlantısı Test Ediliyor...\n")

    try:
        # 1. Herhangi bir şarkıyı isimle aratıyoruz (Playlist kullanmıyoruz)
        print("🎵 'The Weeknd - Blinding Lights' aranıyor...")
        result = sp.search(q="Blinding Lights The Weeknd", type="track", limit=1)
        tracks = result['tracks']['items']

        if not tracks:
            print("❌ Şarkı bulunamadı!")
            return

        track = tracks[0]
        track_id = track['id']
        track_name = track['name']
        artist_name = track['artists'][0]['name']

        print(f"✅ Şarkı Bulundu: {artist_name} - {track_name} (ID: {track_id})")

        # 2. Bulunan şarkının BPM ve Enerji verilerini çekiyoruz
        print("📊 Ses verileri (Audio Features) çekiliyor...")
        features_list = sp.audio_features(track_id)

        if features_list and features_list[0]:
            features = features_list[0]
            bpm = round(features['tempo'])
            energy = round(features['energy'] * 100)
            valence = round(features['valence'] * 100)

            print("\n🎉 BAŞARILI! İŞTE SONUÇLAR:")
            print(f"   ► BPM (Tempo): {bpm}")
            print(f"   ► Enerji: %{energy}")
            print(f"   ► Duygu (Valence): %{valence}")
            print("-" * 40)
        else:
            print("⚠️ Şarkı bulundu ama ses verisi (BPM) çekilemedi.")

    except Exception as e:
        print(f"\n❌ HATA OLUŞTU: {e}")


if __name__ == "__main__":
    test_api_connection()