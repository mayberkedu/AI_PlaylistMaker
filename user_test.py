from data_collection import get_spotify_client

def test_user():
    sp = get_spotify_client()
    try:
        user = sp.current_user()
        print("Logged in as:", user.get('display_name'), user.get('id'))
    except Exception as e:
        print("User error:", e)

if __name__ == "__main__":
    test_user()
