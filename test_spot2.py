import sys
from data_collection import extract_playlist_tracks

def run():
    url = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
    if len(sys.argv) > 1:
        url = sys.argv[1]

    print(f"Testing url: {url}")
    tracks, err = extract_playlist_tracks(url)
    print(f"Count: {len(tracks)}, Err: {err}")
    if tracks:
        print(tracks[0])

if __name__ == "__main__":
    run()
