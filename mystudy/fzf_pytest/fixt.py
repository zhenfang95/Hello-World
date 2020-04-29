#!/usr/bin/env python 

import pytest

#函数式
'''setup_function/teardown_function 每个用例开始和结束调用一次'''
'''setup_module是所有用例开始前只执行一次，teardown_module是所有用例结束后只执行一次'''

def setup_module():
    print('setup_module:整个.py模块开始前执行一次')
    print("比如：所有用例开始前只打开一次浏览器")

def teardown_module():
    print('teardow_module:整个.py模块结束后执行一次')
    print("比如：所有用例结束只最后关闭浏览器")

def setup_function():
    print('setup_function:每个用例开始前都会执行')

def teardown_function():
    print('teardown_function:每个用例结束后都会执行')

def test_01():
    print('执行用例--test_01')
    x='this'
    assert 'h' in x

def test_02():
    print('执行用例--test_02')
    x='hello'
    assert hasattr(x,'check')

def test_03():
    print('执行用例--test_03')
    a='hello'
    b='hello world'
    assert a in b

if __name__ == '__main__':
    pytest.main()