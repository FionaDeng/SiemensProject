__author__ = 'FionaDeng'

import os
from selenium import webdriver
from time import sleep

url = 'https://www.baidu.com'

profile_base_name = os.environ.get('USERPROFILE') + os.sep + "\\AppData\\Roaming\\Mozilla\\FireFox\\Profiles"
for profile_name in profile_base_name:
    if '.default' in profile_name:
        profile_name = os.path.join(profile_base_name,profile_name)
    else:
        profile_name = os.path.join(profile_base_name,"37cppl63.default")

profile = webdriver.FirefoxProfile(profile_name)
driver = webdriver.Firefox(profile)
driver.get(url)
sleep(5)

input_word = driver.find_element_by_xpath("//input[@id='kw']")
input_word.click()
input_word.clear()
input_word.send_keys("balala")

driver.find_element_by_id("su").click()
assert driver.find_element_by_xpath("//img[@title='到百度首']")
sleep(10)

driver.quit()