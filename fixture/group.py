from model.group import Group

class GroupHelper:

	def __init__(self, app):
		self.app = app


	def open_group_page(self):
		wd = self.app.wd
		wd.find_element_by_link_text('Мои классы').click()


	def create(self, group):
		wd = self.app.wd
		self.open_group_page()

		#Начать создание группы
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
			else:
				pass


		#Нажать кнопку Далее
		wd.find_element_by_xpath('//*[@id="new_group"]/div[4]/input').click()

