#!/usr/bin/env python 
import pytest
@pytest.fixture()
def login():
    print("输入账号、密码登录")