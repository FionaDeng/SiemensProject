"""
    前提：按照自动化测试文档，搭建好web测试环境
    使用火狐打开html文件，读取htlm里面p标签的，
    然后用20171122里面进阶题定义的方法分别处理每个p标签，处理完后得到的新的字符串放入列表里面
"""
import os
from selenium import webdriver
from stringExercises import dealWithString

# Note: open html file（modify URL according to its own environment）
# Note: open this url by browser of pycharm
url = 'http://localhost:63342/testProject/getWebParameter/hello.html'
profile_base_dir = os.environ.get('USERPROFILE') + os.sep + "\\AppData\\Roaming\\Mozilla\\FireFox\\Profiles"

for profile_dir in profile_base_dir:
    if '.default' in profile_dir:
        profile_dir = os.path.join(profile_base_dir,profile_dir)
    else:
        profile_dir = os.path.join(profile_base_dir,'37cppl63.default')
profile = webdriver.FirefoxProfile(profile_dir)
driver = webdriver.Firefox(profile)
driver.get(url)

list_word = []
# Note: find_elements_by_css_selector  & find_element_by_css_selector
elements = driver.find_elements_by_css_selector('.pc')
for ele in elements:
    list_word.append(dealWithString.hand_str(ele.text))
driver.quit()
print(list_word)