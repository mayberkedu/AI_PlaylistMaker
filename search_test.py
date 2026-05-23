from data_collection import get_spotify_client
import json

sp = get_spotify_client()
res = sp.search(q='Today', type='playlist', limit=1)
if res and 'playlists' in res and res['playlists']['items']:
    print(res['playlists']['items'])
else:
    print("No items:", res)
