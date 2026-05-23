import requests
from bs4 import BeautifulSoup
import sys

url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print("Looking for JSON data scripts")
ids = [s.get('id') for s in soup.find_all('script') if s.get('id')]
print("Script IDs:", ids)

print("Meta properties:")
metas = [m.get('content') for m in soup.find_all('meta') if m.get('name') == 'music:song']
print("Meta songs found:", len(metas))
sys.stdout.flush()
