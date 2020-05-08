#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/5/8 16:22
# @author:AlexFu

import unittest
from unittest import mock

'''一个已完成开发的功能模拟测试'''
class SubClass(object):
    def add(self, a, b):
        """两个数相加"""
        return a + b

class TestSub(unittest.TestCase):
    """测试两个数相加用例"""
    def test_add2(self):
        # 初始化被测函数类实例
        sub = SubClass()  #可以把这个当成被测接口
        # 创建一个mock对象 return_value代表mock一个数据
        # 传递side_effect关键字参数, 会覆盖return_value参数值, 使用真实的add方法测试
        sub.add = mock.Mock(return_value=15, side_effect=sub.add)
        # 调用被测函数
        result = sub.add(5, 5)
        # 断言实际结果和预期结果
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()