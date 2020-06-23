#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/4/30 16:47
# @author:AlexFu

import pytest
import time

def test_06(start, open_baidu):
    '''测试用例test_06'''
    print("测试用例test_06")
    time.sleep(1)
    assert start == "yoyo"
def test_07(start, open_baidu):
    '''测试用例test_07'''
    print("测试用例test_07")
    time.sleep(1)
    assert start == "yoyo"

if __name__ == "__main__":
    pytest.main(["-s", "test_2.py"])