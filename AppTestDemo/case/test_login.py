#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/7/26 17:11

import unittest,time
from common.sele_location import *
from common.read_yaml import *

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.sele = PySele()

    def test_login(self):
        '''登录模块'''
        self.sele.click('id',getSele(name='btn_login_id'))
        self.sele.clear('class',getSele(name='username_class'))
        self.sele.send_key('class',getSele(name='username_class'),getTest('login','username'))
        self.sele.clear('id',getSele(name='password_id'))
        self.sele.send_key('id',getSele(name='password_id'),getTest('login','password'))
        self.sele.click('id',getSele(name='login_id'))

    def tearDown(self):
        self.sele.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)