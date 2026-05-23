import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

print("Testing Client Credentials:")
ccm = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp_cc = spotipy.Spotify(client_credentials_manager=ccm)
try:
    res = sp_cc.tracks(["6QVAlM2uo9KBuHe2LI3lqX"])
    print("CC Success! Name:", res['tracks'][0]['name'])
except Exception as e:
    print("CC Error", e)

print("\nTesting OAuth:")
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri='http://127.0.0.1:8080', open_browser=False)
sp_oauth = spotipy.Spotify(oauth_manager=auth_manager)
try:
    res = sp_oauth.tracks(["6QVAlM2uo9KBuHe2LI3lqX"])
    print("OAuth Success! Name:", res['tracks'][0]['name'])
except Exception as e:
    print("OAuth Error", e)
