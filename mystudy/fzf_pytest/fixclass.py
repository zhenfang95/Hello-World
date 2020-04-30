#!/usr/bin/env python 
import pytest

class TestClass():
    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def setup_class(self):
        print('setup_class:所有用例执行之前')

    def teardown_class(self):
        print('setup_class:所有用例执行之后')

    def setup_method(self):
        print("setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:  每个用例结束后执行")

    def test_01(self):
        print('执行用例--test_01')
        x = 'this'
        assert 'h' in x

    def test_02(self):
        print('执行用例--test_02')
        x = 'hello'
        assert hasattr(x, 'check')   #hasattr() 函数用于判断对象是否包含对应的属性。

    def test_03(self):
        print('执行用例--test_03')
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main()
