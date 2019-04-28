

class SessionHelper:

	def __init__(self, app):
		self.app = app


	def login(self, username, password):
		wd = self.app.wd
		self.app.open_home_page()
		wd.find_element_by_id('login').send_keys(username)
		wd.find_element_by_id('password').send_keys(password)
		wd.find_element_by_class_name('login-form__submit').click()


	def logout(self):
		wd = self.app.wd
		wd.find_element_by_class_name('headbar--profile').click()
		wd.implicitly_wait(10)
		wd.find_element_by_link_text('Выйти').click()