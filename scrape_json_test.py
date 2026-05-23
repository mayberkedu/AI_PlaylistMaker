import requests
from bs4 import BeautifulSoup

url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print("Looking for JSON data scripts")
found = False
for script in soup.find_all('script'):
    if script.string and 'Spotify' in script.string:
        if 'initial-state' in script.get('id', '') or '__NEXT_DATA__' in script.get('id', ''):
            print("Found script id:", script.get('id'))
            found = True
if not found:
    # Just print the IDs of scripts
    print([s.get('id') for s in soup.find_all('script') if s.get('id')])
