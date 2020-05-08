#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/5/8 16:08
# @author:AlexFu

import unittest
from unittest import mock

'''一个未完成开发的功能模拟测试'''
def add(a,b):
    '''两个数相加'''
    pass

class TestSub(unittest.TestCase):
    '''测试两个数相加用例'''
    def test_sub(self):
        #创建一个mock对象，return_value代表mock一个数据
        mock_add = mock.Mock(return_value=15)
        #将mock对象赋予被测函数
        add = mock_add
        #调用被测函数
        result = add(5,5)
        self.assertEqual(result,15)

if __name__ == '__main__':
    unittest.main()