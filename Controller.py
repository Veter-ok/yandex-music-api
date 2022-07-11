from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Controller():
	def __init__(self) -> None:
		print("___init__)")

	def init_selenium(self, hide):
		options = Options()
		if hide:
			options.headless = True
		self.driver = webdriver.Chrome('/Users/lrd/Desktop/github_projects/yandex-music-api/chromedriver', options=options)

	def get_html(self):
		return self.driver.page_source

	def find_elements(self, className):
		elements = self.driver.find_elements(By.CLASS_NAME, className)
		return elements

	def press_button(self, method, id):
		if method == "class":
			self.driver.find_element(By.CLASS_NAME, id).click()
		elif method == "xpath":
			self.driver.find_element(By.XPATH, id).click()

	def skip_banner(self):
		self.driver.find_element(By.CLASS_NAME,"js-close").click()

	def inputText(self, classInput, text):
		self.driver.find_element(By.CLASS_NAME, classInput).send_keys(text)

	def isElement(self, className):
		element = self.driver.find_element(By.CLASS_NAME, className)
		print(element)
		if element is None:
			return False
		return True