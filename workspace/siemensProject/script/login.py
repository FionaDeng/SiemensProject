import os
from selenium import webdriver
from time import sleep
from libs import data


class Siemens():
    def __init__(self):
        self.driver = self.login(data.url, data.password)

    def login(self, url, password=None, is_login=True):
        # open firefox
        profile_basic_dir = os.environ.get("USERPROFILE") + os.sep + "AppData\\Roaming\\Mozilla\\Firefox\\Profiles"
        for dir_name in os.listdir(profile_basic_dir):
            if '.default' in dir_name:
                profile_dir = os.path.join(profile_basic_dir, dir_name)
                break
            else:
                profile_dir = os.path.join(profile_basic_dir, "ay1z5u29.default")
        profile = webdriver.FirefoxProfile(profile_dir)
        driver = webdriver.Firefox(profile)

        # login
        driver.get(url)
        # driver.implicitly_wait(5)

        if password:
            ele_pwd = driver.find_element_by_id('password')
            ele_pwd.click()
            ele_pwd.send_keys(password)

        if is_login:
            driver.find_element_by_id('login')
        sleep(5)
        return driver

    def __del__(self):
        sleep(3)


if __name__ == '__main__':
    temp = Siemens()


