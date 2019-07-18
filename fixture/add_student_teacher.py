from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddstudentHelper:

	def __init__(self, app):
		self.app = app


	def open_student_page(self):

		wd = self.app.wd
		#  открываю страницу с группами
		self.app.group.ensure_open_group_page()
		# нажимаю кнопку "исправить состав класса (пока что только у 1-го класса в списке)"
		wd.find_element(By.XPATH, '/html/body/section[2]/div[1]/div[1]/div/div[1]/a').click()

	def add_student(self):

		wd = self.app.wd
		self.open_student_page()

		# нажимаю кнопку "добавить ученика"
		wd.find_element(By.CLASS_NAME, 't-students-accounts--button').click()
		#Ввожу фамилию
		wd.find_element(By.CSS_SELECTOR, 'input[placeholder = "Фамилия"]').send_keys('тестовый')
		#Ввожу имя
		wd.find_element(By.CSS_SELECTOR, 'input[placeholder = "Имя"]').send_keys('студент' + Keys.TAB)
		#Нажимаю кнопку добавить
		wd.find_element(By.CSS_SELECTOR, 'button[data-amplitude = "add student"]').click()