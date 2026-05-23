import requests
import json
from bs4 import BeautifulSoup

def get_embed_tracks(pl_id):
    url = f"https://open.spotify.com/embed/playlist/{pl_id}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    with open('out3.txt', 'w', encoding='utf-8') as f:
        f.write(f"Status: {r.status_code}\n")
        f.write(f"Len: {len(r.text)}\n")

        # In the embed, there's usually a script with JSON data
        s = soup.find('script', id='__NEXT_DATA__')
        if s:
            f.write("Found NEXT_DATA\n")
            try:
                data = json.loads(s.string)
                f.write(str(data)[:200] + "...\n")

                # Try navigating to tracks
                # Typically data['props']['pageProps']['state']['data']['entity']['trackList']
                # Let's just dump all track names using regex for debugging
            except Exception as e:
                f.write(f"JSON Error: {e}\n")
        else:
            f.write("No NEXT_DATA found.\n")

        import re
        names = re.findall(r'"name":"([^"]+)"', r.text)
        f.write("Regex found names count: " + str(len(names)) + "\n")
        for n in names[:10]:
            f.write("- " + n + "\n")

get_embed_tracks('37i9dQZF1DXcBWIGoYBM5M')
