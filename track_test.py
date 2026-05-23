from data_collection import get_spotify_client
sp = get_spotify_client()
print("Track test:")
print(sp.track('514joG57v4yKTsfQmz7stz').get('name'))
