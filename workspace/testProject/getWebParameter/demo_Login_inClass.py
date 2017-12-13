__author__ = 'FionaDeng'

import os
from selenium import webdriver
from time import sleep

class Method(object):
    def login_method(self,url):
        profile_base_dir = os.environ.get('USERPROFILE') + os.sep + "\\AppData\\Roaming\\Mozilla\\FireFox\\Profiles"
        for profile_dir in profile_base_dir:
            if '.default' in profile_dir:
                profile_dir = os.path.join(profile_base_dir, profile_dir)
            else:
                profile_dir = os.path.join(profile_base_dir, '37cppl63.default')
        profile = webdriver.FirefoxProfile(profile_dir)
        driver = webdriver.Firefox(profile)
        driver.get(url)

        input_word = driver.find_element_by_xpath("//input[@id='kw']")
        input_word.click()
        input_word.clear()
        input_word.send_keys("balala")

        driver.find_element_by_id("su").click()
        # assert driver.find_element_by_xpath("//img[@title='到百度首']")
        sleep(10)
        # quit browser
        sleep(3)
        driver.quit()


url = 'https://www.baidu.com'

getMethod = Method()
getMethod.login_method(url)


