
import requests
import sys

url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
try:
    r = requests.get(url, headers=headers)
    print("Status:", r.status_code)
    print("Len:", len(r.text))
except Exception as e:
    print(e)
sys.stdout.flush()
