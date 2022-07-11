from requests_html import HTMLSession

class Client():
	def __init__(self, login):
		self.login = login
		self.index_file = 0
		self.session = HTMLSession()


	def __get_html(self, url):
		response = self.session.get(url)
		response.html.render(timeout=20)
		html = response.html
		return html


	def __save_data(self, data, path, name):
		with open(f"{path}{name}.txt", 'w') as file:
			for i in data:
				file.writelines(str(i) + "\n")


	def get_playlist(self, path=None, filename="playlists"):
		url = f"https://music.yandex.ru/users/{self.login}/playlists"
		html = self.__get_html(url)
		names = html.find(".playlist__title-link")
		res = []
		for name in names:
			url_playlist = name.find('a')[0].attrs['href']
			data = {
				"url": f"https://music.yandex.ru{url_playlist}",
				"name": name.text
			}
			res.append(data)
		if not path is None:
			self.__save_data(res, path, filename)
		return res


	def get_tracks_from_playlist(self, url, path=None, filename="playlists"):
		html = self.__get_html(url)
		names = html.find(".d-track__name")
		artists = html.find(".d-track__artists")
		res = []
		for index in range(len(names)):
			data = {
				"name": names[index].text,
				"artist": artists[index].text,
			}
			res.append(data)
		if not path is None:
			self.__save_data(res, path, filename)
		return res


	def get_tracks(self, path=None, filename="playlists"):
		html = self.__get_html(f"https://music.yandex.ru/users/{self.login}/tracks")
		names = html.find(".d-track__name")
		artists = html.find(".d-track__artists")
		res = []
		for index in range(len(names)):
			data = {
				"name": names[index].attrs['title'],
				"artist": artists[index].full_text,
			}
			res.append(data)
		if not path is None:
			self.__save_data(res, path, filename)
		return res
		

	def get_artists(self, path=None, filename="playlists"):
		html = self.__get_html(f"https://music.yandex.ru/users/{self.login}/artists")
		names = html.find(".d-artists")
		muted = html.find(".d-genres")
		res = []
		for index in range(len(names)):
			data = {
				"name": names[index].find('a')[0].text,
				"genres": muted[index].full_text,
			}
			res.append(data)
		if not path is None:
			self.__save_data(res, path, filename)
		return res


	def download_music(self):
		pass