import requests
from bs4 import BeautifulSoup
import json

url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
for m in soup.find_all('meta'):
    # print all og tags
    name = m.get('property') or m.get('name')
    if name and ('music' in name or 'title' in name):
        print(name, "->", m.get('content'))
