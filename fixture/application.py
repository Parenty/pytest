from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.registration import RegHelper
from fixture.add_student_teacher import AddstudentHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'firefox':
            self.wd = webdriver.Firefox()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.wd.maximize_window()
        # self.wd.set_window_size(1300,900)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.registration = RegHelper(self)
        self.addstudent = AddstudentHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
