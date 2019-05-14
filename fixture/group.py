from model.group import Group
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
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
		dropdown = wd.find_element_by_id('group_parallel')
		dropdown.send_keys(group.number_class)


		#Нажать на ссылку "У моего класса нет буквы"
		wd.find_element_by_class_name('toggle_form_part').click()

		#Указать название класса
		wd.find_element_by_id('').send_keys(group.name_class)

		#Выбор предметов в чекбоксах

		for item in group.subject_list:
			if item == 'math':
				wd.find_element_by_xpath('//form[@id="new_group"]/div[3]/div/div[1]').click()
			elif item == 'rus':
				wd.find_element_by_xpath('//form[@id="new_group"]/div[3]/div/div[2]').click()
			elif item == 'eng':
				wd.find_element_by_xpath('//form[@id="new_group"]/div[3]/div/div[3]').click()
			elif item == 'env':
				wd.find_element_by_xpath('//form[@id="new_group"]/div[3]/div/div[4]').click()
			elif item == 'bio':
				wd.find_element_by_xpath('//form[@id="new_group"]/div[3]/div/div[5]').click()
			elif item == 'geo':
				wd.find_element_by_xpath('//form[@id="new_group"]/div[3]/div/div[6]').click()
			elif item == 'soc':
				wd.find_element_by_xpath('//form[@id="new_group"]/div[3]/div/div[7]').click()
			elif item == 'phys':
				wd.find_element_by_xpath('//form[@id="new_group"]/div[3]/div/div[8]').click()
			else:
				pass


		#Нажать кнопку Далее
		wd.find_element_by_xpath('//*[@id="new_group"]/div[4]/input').click()


	def delete_first_group(self):
		wd = self.app.wd
		self.ensure_open_group_page()

		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div[1]/div/div[1]/a').click()
		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[1]/div/div/a').click()

		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		wd.implicitly_wait(10)
		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div[2]/a').click()
		Alert(wd).accept()
		time.sleep(2)


