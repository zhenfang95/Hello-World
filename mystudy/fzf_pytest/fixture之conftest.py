#!/usr/bin/env python 
import pytest

'''@pytest.fixture()里面没有参数，那么默认scope="function"，也就是此时的级别的function，针对函数有效'''
'''scope="function"相当于setup'''
@pytest.fixture()
def login():
    print("输入账号，密码先登录")

def test_s1(login): #每次执行用例前先执行login
    print("用例1：登录后其他操作111")

def test_s2():
    print("用例2：不需要登录，操作222")

def test_s3(login):
    print("用例3：登录后其他操作222")

if __name__ == "__main__":
    pytest.main()