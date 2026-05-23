import requests
import json
from bs4 import BeautifulSoup

def get_embed_tracks(pl_id):
    url = f"https://open.spotify.com/embed/playlist/{pl_id}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    with open('out_json.txt', 'w', encoding='utf-8') as f:
        s = soup.find('script', id='__NEXT_DATA__')
        if s:
            data = json.loads(s.string)
            entity = data.get('props', {}).get('pageProps', {}).get('state', {}).get('data', {}).get('entity', {})
            f.write(json.dumps(entity, indent=2))

get_embed_tracks('37i9dQZF1DXcBWIGoYBM5M')
