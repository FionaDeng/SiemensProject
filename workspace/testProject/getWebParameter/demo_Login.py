__author__ = 'FengqiongDeng'

import os
from selenium import webdriver
from time import sleep

def login_method (url, user_name=None, user_pwd=None,is_open=True):
    profile_base_dir = os.environ.get('USERPROFILE') + os.sep + "\\AppData\\Roaming\\Mozilla\\FireFox\\Profiles"
    for profile_dir in os.listdir(profile_base_dir):
        if '.default' in profile_dir:
            profile_dir = os.path.join(profile_base_dir, profile_dir)
            break
        else:
            profile_dir = os.path.join(profile_base_dir, '37cppl63.default')

    profile = webdriver.FirefoxProfile(profile_dir)
    driver = webdriver.Firefox(profile)
    driver.get(url)

    if user_name:
        user_name = driver.find_element_by_id('login_username')
        user_name.click()
        user_name.clear()
        user_name.send_keys(user_pwd)

    if user_pwd:
        user_pwd = driver.find_element_by_xpath("//input[@type='password']")
        user_pwd.click()
        user_pwd.send_keys(password)

    if is_open:
        driver.find_element_by_class_name("x-btn-center").click()
        sleep(1)

    # quit
    driver.find_element_by_xpath("//button[@type='button']")

    # quit browser
    sleep(3)
    driver.quit()


url = 'http://10.1.77.233/web/dvsc/'
user_name = 'admin'
password = 'admin'
login_method(url,user_name,password)
# assert driver.find_element_by_class_name("x-tab-strip-text ")