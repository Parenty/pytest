import random
import re
import requests
import time

from user import constants


class User:
    def __init__(self, user_type=None, user_email=None, user_password=None, user_name=None, user_data=None, user_url=None, user_region=None, user_query=None):
        self.type = self.check_type(user_type)
        self.name = self.create_name(user_name)
        self.email = self.create_email(user_email)
        #print(self.email)
        self.password = self.create_password(user_password, self.email)
        #print(self.password)
        self.data = self.get_cityes_json(user_url, user_region, user_query)

    # create user fio
    # user_name = :
    #   None or "" or other type => random name
    #   "1 1" => [1, random, 1]
    #   " 1 " => [rnd, 1, rnd]
    #   "1 1 1" =>[1, 1, 1]
    def create_name(self, name):
        first_name  = random.choice(constants.M_NAMES.get("first_name"))
        middle_name = random.choice(constants.M_NAMES.get("middle_name"))
        second_name = random.choice(constants.M_NAMES.get("second_name"))
        try:
            arr_name = name.split(" ")
            return [arr_name[1] if len(arr_name[1]) > 0 else middle_name,
                    arr_name[0] if len(arr_name[0]) > 0 else first_name,
                    arr_name[2] if len(arr_name[2]) > 0 else second_name]
        except (IndexError, AttributeError) as e:
            return [middle_name,
                    first_name,
                    second_name]

    # default role is "teacher"
    # other role is teacher, parent
    def check_type(self, type):
        try:
            if type in constants.ROLE.values():
                return list(constants.ROLE.keys())[list(constants.ROLE.values()).index(type)]
            else:
                return constants.ROLE.get("teacher")
        except (AttributeError, TypeError) as e:
            return constants.ROLE.get("teacher")

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
        if constants.ROLE.get("teacher") == type:
            data = {"tel": "7230498230", "country": "Россия", "region": "", "sity": "", "school": ""}

    # get all cities by region from THIS url (env data)
    def get_cityes_json(self, url, region, query):
        # get cities (rnd|query)
        try:
            if region not in list(constants.REGIONS.keys()):
                if region not in list(constants.REGIONS.values()):
                    region = random.choice(list(constants.REGIONS.items()))
                else:
                    region = list(constants.REGIONS.items())[list(constants.REGIONS.values()).index(region)]
            else:
                region = list(constants.REGIONS.items())[list(constants.REGIONS.keys()).index(region)]
            if type(query) is not str or query is None or query == "":
                query = "г"
        except (AttributeError, TypeError) as e:
            region = random.choice(list(constants.REGIONS.items()))

        url_temp = constants.CITIES.replace("{_baseurl_}", url).replace("{_code_}", region[0]).replace("{_query_}", query)
        cityes = requests.get(url=url_temp).json()

        if len(cityes) is 0 or cityes is None:
            query = "г"
            url_temp = constants.CITIES.replace("{_baseurl_}", url).replace("{_code_}", region[0]).replace("{_query_}", query)
            cityes = requests.get(url=url_temp).json()
        # get school
        if len(cityes)>1:
            city = random.choice(cityes)
        else:
            city = cityes[0]
        print(city)
        return requests.get(url=url_temp).json()

    # todo type value, incorrect value, null value, default value
    def get_schools(self, url, region, city_id, query):
        URL = constants.SCHOOLS.replace("{_baseurl_}", url).replace("{_code_}", region).replace("{_cityID_}", city_id).replace("{_query_}", query)
        print(URL)
        return requests.get(url=URL).json()


# tests
# print(get_city("https://uchi.ru", "29", "г Арханг"))
# print(get_schools("https://uchi.ru", "29", "06814fb6-0dc3-4bec-ba20-11f894a0faf5", "г"))
# User()
# User(user_name="123")
# User(user_name="")
# User(user_name=" 123 123")
# User(user_name="2 2 2")
# User(user_name="  1")
# User(user_name=" ")
# User(user_name="  ")

# User(user_password=None)
# User(user_password=123)
# User()
# User(user_password="123")
s = time.time()
User(user_url="https://uchi.ru", user_region="87", user_query="г Анадырь ")
User(user_url="https://uchi.ru", user_region="Липецкая область", user_query="ш")
User(user_url="https://uchi.ru", user_query="ш")
User(user_url="https://uchi.ru")
User(user_url="https://uchi.ru", user_region="29")
User(user_url="https://uchi.ru", user_region="Архангельская область", user_query="г Архангельск")
User(user_url="https://uchi.ru", user_query="ш")
print(time.time()-s)