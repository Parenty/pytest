from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from model import students


class RegHelper:

    def __init__(self, app):
        self.app = app

    def already_registered(self):
        wd = self.app.wd
        if len(wd.find_elements_by_class_name('form__row-error')) > 0:
            return True

    def reg_teacher(self, registration, students):
        wd = self.app.wd
        wd.find_element_by_class_name('registration-button').click()
        wd.find_element_by_xpath('//*[@id="teacher-select-button"]/div[4]/div').click()
        # ввожу почту
        wd.find_element_by_xpath('//*[@id="teacher_email"]').send_keys(registration.email)

        # ввожу пароль
        wd.find_element_by_xpath('//*[@id="teacher_password"]').send_keys(registration.password)

        # нажать зарегистрироваться
        wd.find_element_by_name('commit').click()

        # Проверяю, не зарегистрирован ли такой учитель
        if self.already_registered():
            return

        # Нажать на кнопку продолжить

        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'form__button')))
        wd.find_element_by_class_name('form__button').click()

        # Ввожу фамилию
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="teacher_last_name"]')))
        wd.find_element_by_xpath('//*[@id="teacher_last_name"]').send_keys('Дмитриев')

        # Ввожу Имя
        wd.find_element_by_xpath('//*[@id="teacher_name"]').send_keys('Иван')

        # Ввожу Отчество
        wd.find_element_by_xpath('//*[@id="teacher_middle_name"]').send_keys('Андреевич')

        # Ввожу номер телефона
        wd.find_element_by_xpath('//*[@id="teacher_phone"]').send_keys('123')

        # Нажимаю кнопку далее
        wd.find_element_by_name('commit').click()

        # Выбор региона
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class = '
                                                                                 '"react-selectize-placeholder"]')))
        wd.find_element(By.XPATH, '/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[3]/div/div/div[2]/input').send_keys("Москва"+ Keys.ENTER)

        WebDriverWait(wd, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[6]/div[1]/div/div[1]')))
        wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/a').click()

        # Ввожу номер школы

        WebDriverWait(wd, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[7]/input')))
        wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[7]/input').send_keys('123')

        # Ввожу название школы
        WebDriverWait(wd, 10).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[8]/textarea')))
        wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[2]/div/div/form/div[8]/textarea').send_keys(
            '123')

        # Нажимаю кнопку далее
        wd.find_element_by_name('commit').click()

        # Создаю группу
        self.app.group.choice_group(registration)

        # Добавляю одного студента
        self.app.addstudent.one_student_registration(students)
