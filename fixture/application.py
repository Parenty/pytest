from selenium import webdriver



class Application:

	def __init__(self):
		self.wd = webdriver.Firefox()
		self.wd.implicitly_wait(60)

	def open_home_page(self):
		wd = self.wd
		wd.get("https://uchi.ru/")

	def login(self, username, password):
		wd = self.wd
		self.open_home_page()
		wd.find_element_by_id('login').send_keys(username)
		wd.find_element_by_id('password').send_keys(password)
		wd.find_element_by_class_name('login-form__submit').click()

	def logout(self):
		wd = self.wd
		wd.find_element_by_class_name('headbar--profile').click()
		self.wd.implicitly_wait(10)
		wd.find_element_by_link_text('Выйти').click()

	def destroy(self):
		self.wd.quit()

