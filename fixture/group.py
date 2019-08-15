from model.group import Group
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.execute_script("window.scrollTo(0, document.body.scrollUp);")
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Мои классы')))
        wd.find_element_by_link_text('Мои классы').click()

    def ensure_open_group_page(self):
        wd = self.app.wd
        if len(wd.find_elements_by_xpath('/html/body/section[2]/div[1]/div[1]/div/div[1]/a')) > 0:
            return
        self.open_group_page()

    def choice_group(self, group):
        wd = self.app.wd
        dropdown = Select(wd.find_element_by_id('group_parallel'))
        dropdown.select_by_value(group.number_class)
        # Нажать на ссылку "У моего класса нет буквы"
        wd.find_element_by_class_name('toggle_form_part').click()

        # Указать название класса
        wd.find_element_by_xpath('//*[@id="new_group"]/div[1]/div[3]/input').send_keys(group.name_class)
        # Выбор предметов в чекбоксах

        for item in group.subject_list:
            if item == 'math':
                wd.find_element_by_css_selector('label[for = "input-checkbox-1"]').click()
            elif item == 'rus':
                wd.find_element_by_css_selector('label[for = "input-checkbox-2"]').click()
            elif item == 'eng':
                wd.find_element_by_css_selector('label[for = "input-checkbox-5"]').click()
            elif item == 'env':
                wd.find_element_by_css_selector('label[for = "input-checkbox-6"]').click()
            elif item == 'prog':
                wd.find_element_by_css_selector('label[for = "input-checkbox-7"]').click()
            elif item == 'bio':
                wd.find_element_by_css_selector('label[for = "input-checkbox-8"]').click()
            elif item == 'geo':
                wd.find_element_by_css_selector('label[for = "input-checkbox-9"]').click()
            elif item == 'soc':
                wd.find_element_by_css_selector('label[for = "input-checkbox-11"]').click()
            elif item == 'phys':
                wd.find_element_by_css_selector('label[for = "input-checkbox-10"]').click()
            elif item == 'chem':
                wd.find_element_by_css_selector('label[for = "input-checkbox-12"]').click()
            elif item == 'hist':
                wd.find_element_by_css_selector('label[for = "input-checkbox-13"]').click()
            else:
                pass

        # Нажать кнопку Далее
        wd.find_element_by_name('commit').click()

    def create(self, group):
        wd = self.app.wd
        self.ensure_open_group_page()

        # Начать создание группы
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wd.find_element_by_class_name('add-class-btn').click()

        self.choice_group(group)

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
        # Проверяю приглашенная группа или нет

        if self.ensure_group_invite():
            wd.find_element_by_xpath('/html/body/div[2]/div[2]/a').click()
        else:
            wd.find_element_by_xpath('/html/body/section[2]/div[1]/div/div[1]/div/div/a').click()

        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wd.implicitly_wait(10)
        wd.find_element_by_xpath('/html/body/section[2]/div[1]/div[2]/a').click()
        Alert(wd).accept()
        time.sleep(2)

    def is_not_registered(self):
        wd = self.app.wd
        if len(wd.find_elements(By.CSS_SELECTOR, 'div[class = "hint"]')) > 0:
            return True
        else:
            return False

    def get_group_list(self):
        wd = self.app.wd
        self.ensure_open_group_page()
        groups = []
        for element in wd.find_elements_by_css_selector('div.section-card_class'):
            # Выделяю только код класса (без лишних слов)
            name_class = element.find_element_by_class_name('section-class__blocks--name').text.split(' ', maxsplit=1)[
                1]
            class_code = element.find_element_by_class_name('class__code').text.split(': ')[1]
            # class_code_list = class_code_text.split(': ')
            # class_code = class_code_list[1]
            # формирую список
            groups.append(Group(name_class=name_class, class_code=class_code))
        return groups
