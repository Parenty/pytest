from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper



class Application:

	def __init__(self):
		self.wd = webdriver.Chrome()
		self.wd.set_window_size(1920,1080)
		self.session = SessionHelper(self)
		self.group = GroupHelper(self)


	def is_valid(self):
		try:
			self.wd.current_url
			return True
		except:
			return False

	def open_home_page(self):
		wd = self.wd
		wd.get("https://uchi.ru/")

	def destroy(self):
		self.wd.quit()

