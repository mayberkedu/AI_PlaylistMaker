import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import lyricsgenius
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import json

# Çevresel değişkenleri yükle
load_dotenv()

def get_spotify_client():
    """Spotify API istemcisini OAuth (Kullanıcı Girişi) ile başlatır."""
    client_id = os.getenv('SPOTIPY_CLIENT_ID')
    client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI', 'http://127.0.0.1:8080') # Varsayılan uri eklendi

    if not client_id or not client_secret:
        raise ValueError("❌ Hata: Spotify API anahtarları eksik.")

    # OAuth Authentication for user playlists
    oauth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-read-private playlist-read-collaborative",
        open_browser=False  # Streamlit ile çakışmaması için tarayıcıyı manuel açmak daha iyidir
    )
    return spotipy.Spotify(oauth_manager=oauth_manager)

def get_genius_client():
    """Genius API istemcisini başlatır ve döndürür."""
    token = os.getenv('GENIUS_ACCESS_TOKEN')
    if not token:
        raise ValueError("❌ Hata: Genius API anahtarı (GENIUS_ACCESS_TOKEN) eksik.")

    genius = lyricsgenius.Genius(token)
    genius.verbose = False  # Konsoldaki kalabalığı önlemek için
    genius.remove_dict = True # Başlık vs. gibi gereksiz teknik bilgileri temizler
    return genius

def extract_playlist_tracks(playlist_url):
    """
    Spotify playlist veya album linkinden şarkı isimlerini (web scraping - embed kullanarak) döndürür.
    Spotify API sınırlarına takılmadan tamamen anonim çalışır!
    """
    tracks_data = []

    try:
        is_album = "album" in playlist_url
        item_type = "album" if is_album else "playlist"

        # Linkten ID'sini ayıkla
        item_id = playlist_url.split("/")[-1].split("?")[0]
        if ":" in item_id:
            item_id = item_id.split(":")[-1]

        # Spotify embed endpoint'ini kullanarak anonim, limitsiz ve API key olmadan çekiyoruz!
        embed_url = f"https://open.spotify.com/embed/{item_type}/{item_id}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

        r = requests.get(embed_url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        script = soup.find('script', id='__NEXT_DATA__')

        # Eğer NEXT_DATA boşta kalır veya trackList yoksa, kullanıcının linkte playlist yazıp albüm ID'si (veya tam tersi)
        # vermiş olma ihtimaline karşı diğer türü deneyelim.
        data = json.loads(script.string) if script else {}
        entity = data.get('props', {}).get('pageProps', {}).get('state', {}).get('data', {}).get('entity', {})
        track_list = entity.get('trackList', [])

        if not track_list:
            alt_type = "playlist" if item_type == "album" else "album"
            alt_embed_url = f"https://open.spotify.com/embed/{alt_type}/{item_id}"
            r_alt = requests.get(alt_embed_url, headers=headers)
            soup_alt = BeautifulSoup(r_alt.text, 'html.parser')
            script_alt = soup_alt.find('script', id='__NEXT_DATA__')
            if script_alt:
                data_alt = json.loads(script_alt.string)
                entity = data_alt.get('props', {}).get('pageProps', {}).get('state', {}).get('data', {}).get('entity', {})
                track_list = entity.get('trackList', [])

        if not track_list:
            return [], f"Liste verisi okunamadı. 404 Hatalı link veya Özel/Gizli liste olabilir."

        for track in track_list:
            if track.get('entityType') == 'track':
                title = track.get('title')
                # Spotify embed, sanatçıları "subtitle" alanında virgülle ya da birlikte verir
                subtitle = track.get('subtitle', '').replace('\u00a0', ' ')
                artists = [a.strip() for a in subtitle.split(',')] if subtitle else ["Bilinmeyen Sanatçı"]

                if title:
                    tracks_data.append({
                        "track_name": title,
                        "artist": artists[0],
                        "all_artists": artists
                    })

        if not tracks_data:
            return [], "Link içinde hiçbir şarkı okunamadı."

        return tracks_data, None

    except Exception as e:
        error_msg = f"Web Scraping Hatası: {str(e)}"
        print(error_msg)
        return [], error_msg

def get_lyrics(track_name, artist_name):
    """
    Verilen şarkı adı ve sanatçı ismiyle Genius üzerinden şarkı sözlerini çeker.
    Args:
        track_name (str): Şarkı adı.
        artist_name (str): Sanatçı adı.
    Returns:
        str or None: Şarkı sözleri metni veya bulunamazsa None.
    """
    try:
        genius = get_genius_client()
        song = genius.search_song(track_name, artist_name)
        if song:
            return song.lyrics
        return None
    except Exception as e:
        print(f"'{track_name}' şarkı sözleri çekilirken hata oluştu: {e}")
        return None

if __name__ == "__main__":
    # Kısa bir test
    print("Müzik Veri Toplama Modülü Yüklendi.")
