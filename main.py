from tests import *

if __name__ == "__main__":
	client = Client("lrd.msk")
	playlists = client.get_playlists(save=True)
	# for playlist in playlists:
	# 	print(f"[INFO] playlist {playlist['name']}")
	# 	musics = client.get_tracks_from_playlist(playlist['url'])
	# 	print(f"[INFO] количество песен {len(musics)}")
	# 	for j in musics:
	# 		print(j)
	# tracks = client.get_tracks()
	# print(len(tracks))
	# for i in tracks:
	# 	print(i)
	# artists = client.get_artists()
	# print(len(artists))
	# for i in artists:
	# 	print(i)