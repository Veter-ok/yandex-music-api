from time import sleep
from Controller import Controller

class LoginUser(Controller):
	def __init__(self, login, password):
		self.init_selenium(False)
		self.login = login
		self.password = password
		self.__login()

	def __login(self):
		self.driver.get("https://passport.yandex.ru/auth?origin=music_button-header&retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Freqid%3D2849352716571027076559326272591761%26from-passport")
		try:
			self.inputText("Textinput-Control", self.login + "\n")
			sleep(2)
			self.inputText("Textinput-Control", self.password + "\n")
			if self.isElement("Button2_type_submit"):
				print("------start-----")
				self.press_button("class", "Button2_type_submit")
			print("------end-----")
		except:
			print("-------Ошибка при в ходе в аккаунт-------") 

	def get_playlists(self):
		self.press_button("xpath", "/html/body/div[1]/div[7]/div/div/div[2]/div[1]/div/a[5]")
		sleep(3)
		names = self.find_elements("playlist__title-link")
		links = self.find_elements("playlist__title-cover")
		res = []
		for index in range(len(names)):
			url_playlist = links[index].get_attribute('href')
			data = {
				"name": names[index].text,
				"url": url_playlist,
			}
			res.append(data)
		return res