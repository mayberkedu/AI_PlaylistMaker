import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI', 'http://127.0.0.1:8080')

print("Spotify yetkilendirmesi başlatılıyor...")

sp_oauth = SpotifyOAuth(client_id=client_id,
                        client_secret=client_secret,
                        redirect_uri=redirect_uri,
                        scope="playlist-read-private playlist-read-collaborative",
                        open_browser=True)

# Bu işlem tarayıcıda bir sekme açacak. Uygulamaya izin verdiğinizde
# sizi yönlendireceği adresin linkini kopyalayıp terminale yapıştırmanız istenecek (veya otomatik algılayacak).
token = sp_oauth.get_access_token(as_dict=False)

if token:
    print("✅ Başarılı! Cache dosyası oluşturuldu. Artık Streamlit uygulamanızı sorunsuzca kullanabilirsiniz.")
else:
    print("❌ Token alınamadı.")
