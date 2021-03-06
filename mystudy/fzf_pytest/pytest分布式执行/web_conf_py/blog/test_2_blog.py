#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/4/30 16:50
# @author:AlexFu

import pytest
import time

def test_03(start, open_blog):
    '''测试用例test_03'''
    print("测试用例test_03")
    time.sleep(1)
    assert start == "yoyo"

def test_04(start, open_blog):
    '''测试用例test_04'''
    print("测试用例test_04")
    time.sleep(1)
    assert start == "yoyo"

def test_05(start, open_blog):
    '''跨模块调用baidu模块下的conftest'''
    print('测试用例test_05，跨模块调用baidu')
    time.sleep(1)
    assert start == 'yoyo'

if __name__ == '__main__':
    pytest.main(["-s","test_2_blog.py"])