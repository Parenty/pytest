from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from model.students import Students
import time


class AddstudentHelper:

    def __init__(self, app):
        self.app = app

    def open_student_page(self):
        wd = self.app.wd
        #  открываю страницу с группами
        self.app.group.ensure_open_group_page()
        # нажимаю кнопку "исправить состав класса (пока что только у 1-го класса в списке)"
        WebDriverWait(wd, 10).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/section[2]/div[1]/div[1]/div/div[1]/a')))
        wd.find_element(By.XPATH, '/html/body/section[2]/div[1]/div[1]/div/div[1]/a').click()

    def one_student_registration(self, students):  # Добавление студента при регистрации

        wd = self.app.wd
        # Ввожу фамилию
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder = "Фамилия"]').send_keys(students.student_surname)
        # Ввожу имя
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder = "Имя"]').send_keys(students.student_name + Keys.TAB)
        # Нажимаю кнопку добавить
        wd.find_element(By.CSS_SELECTOR, 'button[data-amplitude = "add student"]').click()
        # Нажимаю на кнопку готово
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value = "Готово"]')))
        wd.find_element(By.CSS_SELECTOR, 'input[value = "Готово"]').click()

        WebDriverWait(wd, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value = "Перейти в личный кабинет"]')))
        wd.find_element(By.CSS_SELECTOR, 'input[value = "Перейти в личный кабинет"]').click()

    def one_student(self, students):  # Добавление студента уже зарегистрированному учителю

        wd = self.app.wd
        # Ввожу фамилию
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder = "Фамилия"]').send_keys(students.student_surname)
        # Ввожу имя
        wd.find_element(By.CSS_SELECTOR, 'input[placeholder = "Имя"]').send_keys(students.student_name + Keys.TAB)
        # Нажимаю кнопку добавить
        wd.find_element(By.CSS_SELECTOR, 'button[data-amplitude = "add student"]').click()
        time.sleep(1)

    def add_student(self, students):
        wd = self.app.wd
        self.ensure_open_student_page()
        if EC.element_to_be_clickable((By.CLASS_NAME, 't-students-accounts--button')):
            wd.find_element(By.CLASS_NAME, 't-students-accounts--button').click()
        self.one_student(students)

    def ensure_open_student_page(self):
        wd = self.app.wd
        if len(wd.find_elements(By.CLASS_NAME, 't-students-accounts--button')) > 0:
            return
        self.open_student_page()

    def get_students_list(self):
        wd = self.app.wd
        self.ensure_open_student_page()
        students = []
        for element in wd.find_elements(By.CLASS_NAME, 't-students-accounts--row'):
            num_student = element.find_element(By.CSS_SELECTOR,
                                               '#edit_student > div.t-students-accounts--item.num').text
            password_student = element.find_element(By.CSS_SELECTOR,
                                                    '#edit_student > div.t-students-accounts--item.password').text
            students.append(Students(num_student=num_student, password_student=password_student))
        return students
