import requests
import json
from bs4 import BeautifulSoup

url = "https://open.spotify.com/embed/album/62e42RyXywke5INCA3VRGJ"
r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(r.text, 'html.parser')
s = soup.find('script', id='__NEXT_DATA__')
with open('debug_out.txt', 'w', encoding='utf-8') as f:
    if s:
        data = json.loads(s.string)
        f.write(json.dumps(data.get('props', {}).get('pageProps', {}).get('state', {}).get('data', {}).get('entity', {}), indent=2))
    else:
        f.write("No NEXT DATA")
