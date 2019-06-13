from selenium.webdriver.common.keys import Keys
import time

class RegHelper:

	def __init__(self, app):
		self.app = app


	def reg_teacher(self):
		wd = self.app.wd
		wd.find_element_by_class_name('registration-button').click()
		wd.find_element_by_xpath('//*[@id="teacher-select-button"]/div[4]/div').click()
		#ввожу почту
		wd.find_element_by_xpath('//*[@id="teacher_email"]').send_keys('11222222222222u@uchi.ru')

		#ввожу пароль
		wd.find_element_by_xpath('//*[@id="teacher_password"]').send_keys('123')

		#нажать зарегистрироваться
		wd.find_element_by_name('commit').click()

		#Нажать на кнопку продолжить
		time.sleep(5)
		wd.find_element_by_css_selector('.form__button').click()

		#Ввожу фамилию
		wd.find_element_by_xpath('//*[@id="teacher_last_name"]').send_keys('Дмитриев')

		#Ввожу Имя
		wd.find_element_by_xpath('//*[@id="teacher_name"]').send_keys('Иван')

		#Ввожу Отчество
		wd.find_element_by_xpath('//*[@id="teacher_middle_name"]').send_keys('Андреевич')

		#Ввожу номер телефона
		wd.find_element_by_xpath('//*[@id="teacher_phone"]').send_keys('123')

		#Нажимаю кнопку далее
		wd.find_element_by_name('commit').click()

		#Выбираю регион
		#wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[3]/div/div[1]/div[2]/input').send_keys('Архангельская область')
		#time.sleep(1)
		#wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[3]/div/div[1]/div[2]/input').send_keys(Keys.DOWN)
		#wd.find_element_by_class_name('dropdown-menu default react-selectize simple-select regular-font').send_keys(Keys.ENTER)
		time.sleep(2)
		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[3]/div').click()
		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[3]/div/div[2]/div[1]').click()
		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/a').click()

		#Ввожу номер школы
		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[7]/input').send_keys('123')

		#Ввожу название школы
		wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[8]/textarea').send_keys('123')

		#Нажимаю кнопку далее
		wd.find_element_by_name('commit').click()




		