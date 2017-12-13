__author__ = 'FengqiongDeng'

import os
from time import sleep
from selenium import webdriver

# siemens web service
url = 'http://10.1.77.233/web/dvsc/'

# get profile direct path
profile_base_dir = os.environ.get('USERPROFILE') + os.sep + "\\AppData\\Roaming\\Mozilla\\FireFox\\Profiles"
for profile_dir in profile_base_dir:
    if '.default' in profile_dir:
        profile_dir = os.path.join(profile_base_dir,profile_dir)
    else:
        profile_dir = os.path.join(profile_base_dir,'37cppl63.default')

profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox(profile)
driver.get(url)

# implicit waiting 隐式等待:当查找元素或元素没有立即出现时，先隐式等待10秒再查找DOM，默认时间为0
# driver.implicitly_wait(15)

# username
user_name = driver.find_element_by_id('login_username')
user_name.click()
user_name.clear()
user_name.send_keys('admin')

# password
user_pwd = driver.find_element_by_xpath("//input[@type='password']")
user_pwd.click()
user_pwd.send_keys('admin')

# submit button
login_btn = driver.find_element_by_class_name("x-btn-center").click()

sleep(1)

assert driver.find_element_by_class_name("x-tab-strip-text ")

# quit
driver.find_element_by_xpath("//button[@type='button']")

# quit browser
sleep(3)
driver.quit()







