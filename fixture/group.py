from model.group import Group
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
#from selenium.webdriver.support.ui import Select
import time

class GroupHelper:

	def __init__(self, app):
		self.app = app


	def open_group_page(self):
		wd = self.app.wd
		wd.find_element_by_link_text('Мои классы').click()

	def ensure_open_group_page(self):
		wd = self.app.wd
		if len(wd.find_elements_by_xpath('/html/body/section[2]/div[1]/div[1]/div/div[1]/a')) > 0:
			return
		self.open_group_page()


	def create(self, group):
		wd = self.app.wd
		self.ensure_open_group_page()

		#Начать создание группы
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		wd.find_element_by_class_name('add-class-btn').click()

		#Выбираю нужный номер класса

		dropdown = wd.find_element_by_id('select2-group_parallel-container')
		dropdown.click()
		wd.find_element_by_class_name('select2-search__field').send_keys(group.number_class)
		wd.find_element_by_class_name('select2-search__field').send_keys(Keys.ENTER)


		#Нажать на ссылку "У моего класса нет буквы"
		wd.find_element_by_class_name('toggle_form_part').click()

		#Указать название класса
		wd.find_element_by_xpath('//*[@id="new_group"]/div[1]/div[3]/input').send_keys(group.name_class)
		#Выбор предметов в чекбоксах

		for item in group.subject_list:
			if item == 'math':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[1]').click()
			elif item == 'rus':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[2]').click()
			elif item == 'eng':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[3]').click()
			elif item == 'env':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[4]').click()
			elif item == 'prog':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[5]').click()
			elif item == 'bio':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[6]').click()
			elif item == 'geo':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[7]').click()
			elif item == 'soc':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[8]').click()
			elif item == 'phys':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[9]').click()
			elif item == 'chem':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[10]').click()
			elif item == 'hist':
				wd.find_element_by_xpath('//*[@id="new_group"]/div[2]/div/div[11]').click()
			else:
				pass


		#Нажать кнопку Далее
		wd.find_element_by_name('commit').click()

		#Метод который проверяет приглашенная группа или нет
	def ensure_group_invite(self):
		wd = self.app.wd
		if len(wd.find_elements_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/form/div[2]/div[3]/input')) > 0:
			return True
		else:
			return False


	def delete_first_group(self):
		wd = self.app.wd
		self.ensure_open_group_page()

		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div[1]/div/div[1]/a').click()
		## Проверяю приглашенная группа или нет

		if self.ensure_group_invite() == True:
			wd.find_element_by_xpath('/html/body/div[2]/div[2]/a').click()
		else:
			wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[1]/div/div/a').click()

		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		wd.implicitly_wait(10)
		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div[2]/a').click()
		Alert(wd).accept()
		time.sleep(2)


	def get_group_list(self):
		wd = self.app.wd
		self.ensure_open_group_page()
		groups = []
		for element in wd.find_elements_by_css_selector('div.section-card_class'):
			#Выделяю только название класса (без номера)
			text = element.find_element_by_class_name('section-class__blocks--name').text
			text_list = text.split(' ', maxsplit = 1)
			name_class = text_list[1]
			#Выделяю только код класса (без лишних слов)
			class_code_text = element.find_element_by_class_name('class__code').text
			class_code_list = class_code_text.split(': ')
			class_code = class_code_list[1]
			#формирую список
			groups.append(Group(name_class = name_class, class_code = class_code))
		return groups




