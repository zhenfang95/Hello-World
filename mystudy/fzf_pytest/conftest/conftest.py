#!/usr/bin/env python 
import pytest
'''conftest.py文件名称时固定的，pytest会自动识别该文件。放到项目的根目录下就可以全局调用了'''
@pytest.fixture()
def login():
    print("输入账号、密码登录")