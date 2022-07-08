from User import Client
from LoginUser import LoginUser
from time import sleep

def user_get_playlists():
	client = Client("lrd.msk")
	res = client.get_playlists()
	return res

def user_get_music(url):
	client = Client("lrd.msk")
	musics = client.get_music_from_playlist(url)
	print(f"[INFO] количество песен {len(musics)}")
	return musics

def user_login_get_playlists():
	client = LoginUser("lrd-msk", "Vthrehbq@2006.he")
	sleep(5)
	playlists = client.get_playlists()
	for i in playlists:
		print(i)