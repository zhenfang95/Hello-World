#!/usr/bin/env python 
import pytest

'''不需要import导入 conftest.py模块，pytest用例会自动查找'''
def test_s1(login):
    print("用例1：登录之后其它动作111")

def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")

def test_s3(login):
    print("用例3：登录之后其它动作333")

if __name__ == "__main__":
    pytest.main()