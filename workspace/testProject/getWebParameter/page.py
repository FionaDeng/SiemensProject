"""
    西门子服务器对应的web端界面封装
"""
import os
from time import sleep
from utils.settings import *
from selenium import webdriver
from selenium.webdriver.support.select import Select

class Simens(object):
    def __init__(self, url=url, user=username, password=password):
        self.url = url
        self.user = user
        self.password = password
        self.driver = self.login(self.url, self.user, self.password)

    def login(self, url, user=None, password=None, is_login=True):
        # open firefox
        profile_base_dir = os.environ.get('USERPROFILE') + os.sep + "AppData\\Roaming\\Mozilla\\Firefox\\Profiles"
        for dir_name in os.listdir(profile_base_dir):
            if '.default' in dir_name:
                profile_dir = os.path.join(profile_base_dir, dir_name)
                break
            else:
                profile_dir = os.path.join(profile_base_dir, 'tvumvzbj.default')
        profile = webdriver.FirefoxProfile(profile_dir)
        driver = webdriver.Firefox(profile)
        # login
        driver.get(url)
        driver.implicitly_wait(5)
        if user:
            ele_user = driver.find_element_by_id('login_username')
            ele_user.click()
            ele_user.send_keys(user)
        if password:
            ele_password = driver.find_element_by_id('ext-comp-1005')
            ele_password.click()
            ele_password.send_keys(password)
        if is_login:
            driver.find_element_by_id('ext-gen56').click()
        sleep(1)
        return driver

    def __del__(self):
        sleep(3)
        self.driver.quit()

    def sm_enter_surface(self, surface):
        """
        登录后进入各个功能界面
        :param surface: 如'基础数据', '终端管理'
        :return:
        """
        self.driver.find_element_by_xpath("//span[contains(., '%s')]" % surface).click()

    def sm_data_delete(self):
        self.sm_enter_surface('基础数据')
        self.driver.find_element_by_css_selector('div.x-grid3-hd-inner.x-grid3-hd-checker div.x-grid3-hd-checker').click()
        self.driver.find_element_by_css_selector('button.x-btn-text.icon-delete').click()
        try:
            self.driver.find_element_by_xpath("//button[contains(., 'Yes')]").click()
            sleep(3)
        except:
            self.driver.find_element_by_xpath("//button[contains(., 'OK')]").click()

    def sm_data_init(self, is_del_first=True, issue=None, zone=None, build=None, unit=None, floor=None, room=None):
        self.sm_enter_surface('基础数据')
        if is_del_first:
            self.sm_data_delete()
        # 点击初始化
        self.driver.find_element_by_css_selector('button.x-btn-text.icon-init').click()
        if issue:
            ele_issue = self.driver.find_element_by_name('qinum')
            ele_issue.click()
            ele_issue.clear()
            ele_issue.send_keys(str(issue))
        if zone:
            ele_zone = self.driver.find_element_by_name('zonenum')
            ele_zone.click()
            ele_zone.clear()
            ele_zone.send_keys(str(zone))
        if build:
            ele_build = self.driver.find_element_by_name('buildingnum')
            ele_build.click()
            ele_build.clear()
            ele_build.send_keys(str(build))
        if unit:
            ele_unit = self.driver.find_element_by_name('unitnum')
            ele_unit.click()
            ele_unit.clear()
            ele_unit.send_keys(str(unit))
        if floor:
            ele_floor = self.driver.find_element_by_name('floornum')
            ele_floor.click()
            ele_floor.clear()
            ele_floor.send_keys(str(floor))
        if room:
            ele_room = self.driver.find_element_by_name('roomnum')
            ele_room.click()
            ele_room.clear()
            ele_room.send_keys(str(room))
        sleep(0.1)
        self.driver.find_element_by_xpath("//button[contains(.,'添加')]").click()
        sleep(5)

    def sm_get_device(self, type=None):
        # 点击终端管理
        self.driver.find_element_by_xpath(".//*[@id='mainPanel__img-chooser-dlg']/a[2]/em/span/span").click()# 点击中断管理
        # 是否分类检索
        if type:
            self.driver.find_element_by_id('devicesType').click()   # 选择设备类型
            sleep(1)
            self.driver.find_element_by_xpath("//div[contains(.,'%s')]"% type).click()
            sleep(0.5)
        terms = self.driver.find_elements_by_class_name("thumb-wrap")
        print(terms)
        dev_list = []
        for term in terms:
            dev_id = term.text
            dev_list.append(dev_id)
        return dev_list

    def sm_add_location(self, location, count):
        """
        基础数据添加, location为区则添加栋
        :param location: '0001区'， ‘0001栋’
        :return:
        """
        while 1:
            try:
                self.driver.find_element_by_class_name('x-tree-ec-icon x-tree-elbow-end-plus').click()
            except:
                break
        if location:
            self.driver.find_element_by_xpath("//span[contains(.,'%s')]"% location).click()
            for member in scope:
                if member in location:
                    sub_loc = next(scope)   # 期->区->栋->单元
                    break
        # 点击基础数据
        self.driver.find_element_by_xpath("//span[contains(., '%s')]" % '基础数据').click()
        exists_data =self.driver.find_elements_by_class_name('x-grid3-cell-inner x-grid3-col-2')
        if len(exists_data) <= count:
            nonexist = count - len(exists_data)

        else:
            raise Exception('exists data is enough, do not need to add more.')

if __name__ == "__main__":
    sm = Simens()


