from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper



class Application:

	def __init__(self, browser='chrome'):
		if browser == 'chrome':
			self.wd = webdriver.Chrome()
		elif browser == 'firefox':
			self.wd = webdriver.Firefox()
		else:
			raise ValueError('Unrecognized browser %s' % browser)
		self.wd.set_window_size(1300,900)
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

