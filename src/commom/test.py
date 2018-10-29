#!D:\Python\python.exe
# _*_coding:utf-8_*_
# author:huxiaobo
import unittest
from Test_guanaijiajia.src.commom import driver_configure

class Test(unittest.TestCase):
    def setUp(self):
        cls = driver_configure.driver_configure
        a = cls.get_driver();
        print(a)