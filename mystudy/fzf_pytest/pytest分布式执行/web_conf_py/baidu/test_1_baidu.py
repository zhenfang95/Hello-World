#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/4/30 16:43
# @author:AlexFu

import pytest
import time

def test_01(start,open_baidu):
    '''测试用例test_01'''
    print('测试用例test_01')
    time.sleep(1)
    assert start == 'yoyo'

def test_02(start,open_baidu):
    '''测试用例test_02'''
    print('测试用例test_02')
    time.sleep(1)
    assert start == 'yoyo'

if __name__ == '__main__':
    pytest.main(["-s","test_1_baidu.py"])

