import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Default Top Hits
url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
playlist_id = url.split("/")[-1].split("?")[0]
if ":" in playlist_id:
    playlist_id = playlist_id.split(":")[-1]

print("Looking up:", playlist_id)
try:
    res = sp.playlist(playlist_id)
    print("Playlist Name:", res.get("name"))
except Exception as e:
    print("Error playlist():", e)

try:
    res2 = sp.playlist_items(playlist_id)
    print(f"Items found: {len(res2.get('items', []))}")
except Exception as e:
    print("Error playlist_items():", e)

print("Searching playlists...")
try:
    search_res = sp.search(q="Top Hits", type="playlist", limit=1)
    print("Search Result:", search_res)
    if search_res['playlists']['items']:
        p_id = search_res['playlists']['items'][0]['id']
        print("Found Playlist ID:", p_id)
        # Try fetching this playlist
        pl = sp.playlist(p_id)
        print("Fetched successfully:", pl['name'])
except Exception as e:
    print("Search or fetch error:", e)
