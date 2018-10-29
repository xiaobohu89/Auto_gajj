#!G:\python\python.exe
# _*_coding: utf-8 _*_
# author: huxiaobo

import os
import time
import unittest
# import sys
# sys.path.append('E:\\Work\\Workspace-python\\Test_guanaijiajia\\src\\commom')
from Auto_gajj.src.commom import driver_configure
from appium import webdriver

class Test(unittest.TestCase):
    def setUp(self):
        # print ('initialize!')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'   #测试机Android版本
        desired_caps['deviceName'] = 'b2b4487b'   #测试机序列号 adb devices   vivo:b2b4487b
        desired_caps['appPackage'] = 'com.ithooks.android.ccbxreap'     #被测app包名
        desired_caps['appActivity'] = 'com.ithooks.android.ccbxreap.ui.index.ActivityIndex'#app启动的activity
        desired_caps['newCommandTimeout'] = '300'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        # print 'open app!'
        time.sleep(10)

    def test01(self):
        u'''进入登录页面'''
        self.driver.find_element_by_id("com.ithooks.android.ccbxreap:id/tv_login").click()
        time.sleep(3)
        # self.driver.find_element_by_id("com.ithooks.android.ccbxreap:id/toolbar_title").click()
        self.driver.find_element_by_id("com.ithooks.android.ccbxreap:id/et_phone").send_keys('18100000012')
        self.driver.find_element_by_id("com.ithooks.android.ccbxreap:id/et_pwd").send_keys('888888')
        self.driver.get_screenshot_as_file('before_login.png')
        self.driver.find_element_by_id("com.ithooks.android.ccbxreap:id/btn_login").click()
        time.sleep(10)
        self.driver.get_screenshot_as_file('after_login.png')

    # def test02(self):
    #     u'''页面返回键退出铃音设置页面'''
    #     self.driver.find_element_by_id("com.tyuan.tangy:id/title").click()
    #     time.sleep(5)
    #     self.driver.find_element_by_id("com.tyuan.tangy:id/img_back").click()
    #     time.sleep(5)
    # def test03(self):
    #     u'''系统返回键退出铃音设置页面'''
    #     self.driver.find_element_by_id("com.tyuan.tangy:id/title").click()
    #     time.sleep(5)
    #     self.driver.press_keycode(4)         #系统返回键代码为4
    #     time.sleep(5)
    def tearDown(self):
        self.driver.quit()
        # print "close app!"
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()
