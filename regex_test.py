import requests
from bs4 import BeautifulSoup
import re

url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')

print("Looking for title and artist in script tags...")
# Check if track names exist in the raw HTML string
matches = re.finditer(r'"track":\{"name":"(.*?)".*?"artists":\[\{"name":"(.*?)"', r.text)
found = 0
for m in matches:
    print(f"{m.group(1)} - {m.group(2)}")
    found += 1
    if found >= 5: break

if found == 0:
    for s in soup.find_all('meta'):
        if s.get('property') == 'music:song':
            print("Found song meta:", s.get('content'))
