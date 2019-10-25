import random
import re
import requests
import constant


class User:
    def __init__(self, user_type=None, user_email=None, user_password=None, user_name=None, user_data=None):
        self.type = self.check_type(user_type)
        self.name = self.create_name(user_name)
        self.email = self.create_email(user_email)
        self.password = self.create_password(user_password, self.email)
        self.data = self.create_userdata(self.type, user_data)

    # create user fio
    # user_name = :
    #   None or "" or other type => random name
    #   "1 1" => [1, random, 1]
    #   " 1 " => [rnd, 1, rnd]
    #   "1 1 1" =>[1, 1, 1]
    def create_name(self, name):
        first_name = constant.M_NAMES.get("first_name")[random.randint(0, len(constant.M_NAMES.get("first_name"))) - 1]
        middle_name = constant.M_NAMES.get("middle_name")[
            random.randint(0, len(constant.M_NAMES.get("first_name"))) - 1]
        second_name = constant.M_NAMES.get("second_name")[
            random.randint(0, len(constant.M_NAMES.get("first_name"))) - 1]
        try:
            arr_name = name.split(" ")
            return [arr_name[0] if len(arr_name[0]) > 0 else first_name,
                    arr_name[1] if len(arr_name[1]) > 0 else middle_name,
                    arr_name[2] if len(arr_name[2]) > 0 else second_name]
        except (IndexError, AttributeError) as e:
            return [first_name,
                    middle_name,
                    second_name]

    # default role is "teacher"
    # other role is teacher, parent
    def check_type(self, type):
        try:
            if type in constant.ROLE.values():
                return list(constant.ROLE.keys())[list(constant.ROLE.values()).index(type)]
            else:
                return constant.ROLE.get("teacher")
        except (AttributeError, TypeError) as e:
            return constant.ROLE.get("teacher")

    # random or input
    def create_email(self, email):
        l0 = 99999
        l1 = 99999999999
        try:
            if type(email) is str and re.match("([A-Za-z0-9+=_.]+)[@]([A-Za-z0-9+=_.]+)[.]([A-Za-z0-9+=_.]+)", email):
                return email
            else:
                return str(random.randint(l0, l1)) + "@" + str(random.randint(l0, l1)) + ".ru"
        except (AttributeError, TypeError) as e:
            return str(random.randint(l0, l1)) + "@" + str(random.randint(l0, l1)) + ".ru"

    # default password = email
    def create_password(self, password, email):
        if password is None or type(password) is not str or password == "":
            return email
        else:
            return password

    # teacher:
    #   tel
    #   country => region => sity => school
    #   todo teacher|school abtests
    # parent:
    #   tel
    #   role(b2t => teacher_code|b2c(default))
    #   todo student|parent(?) abtests
    def create_userdata(self, type, user_data):
        if constant.ROLE.get("teacher") == type:
            data = {"tel": "7230498230", "country": "Россия", "region": "", "sity": "", "school": ""}

    # todo type value, incorrect value, null value, default value
    def get_cities(self, url, region, query):
        URL = constant.CITIES.replace("{_baseurl_}", url).replace("{_code_}", region).replace("{_query_}", query)
        return requests.get(url=URL).json()

    # todo type value, incorrect value, null value, default value
    def get_schools(self, url, region, city_id, query):
        URL = constant.SCHOOLS.replace("{_baseurl_}", url).replace("{_code_}", region).replace("{_cityID_}", city_id).replace("{_query_}", query)
        print(URL)
        return requests.get(url=URL).json()


# tests
#print(get_cities("https://uchi.ru", "29", "г Арханг"))
#print(get_schools("https://uchi.ru", "29", "06814fb6-0dc3-4bec-ba20-11f894a0faf5", "г"))
# User()
# User(user_password="123")
# User(user_password="")
# User(user_password=123)
# User(user_email="11@11.ru", user_password="123")
# User(user_email="11@11.ru", user_password="")
# User(user_email="11@11.ru", user_password=123)
# User(user_email="11@11.ru")
# User(user_email="@11.ru", user_password="123")
# User(user_email="11.ru11@", user_password="")
# User(user_email="11.ru11@", user_password=123)
# User(user_email="11.ru11@")
# User(user_email=123, user_password="123")
# User(user_email=123, user_password="")
# User(user_email=123, user_password=123)
# User(user_email=123)
