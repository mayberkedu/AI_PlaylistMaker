import requests
from bs4 import BeautifulSoup
import json

url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
try:
    r = requests.get(url, headers=headers)
    print("Status:", r.status_code)

    # We can search for the tracks in the HTML
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('title')
    print("Title:", title.text if title else "No title")

    # There's usually a <script type="application/json" id="__NEXT_DATA__"> or `<meta name="music:song" content="...`
    # Let's count track metas
    metas = soup.find_all('meta', attrs={"name": "music:song"})
    print("Found meta songs:", len(metas))
    if metas:
        print("Example string:", metas[0].get('content'))
except Exception as e:
    print(e)
