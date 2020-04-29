#!/usr/bin/env python 
import pytest

'''不需要import导入 conftest.py模块，pytest用例会自动查找'''
def test_s4(login):
    print("用例4：登录之后其它动作111")

def test_s5():  # 不传login
    print("用例5：不需要登录，操作222")

if __name__ == "__main__":
    pytest.main()