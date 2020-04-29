#!/usr/bin/env python

import pytest

class TestClass():
    def test_one(self):
        x = 'this'
        assert 'h' in x

    def test_two(self):
        x= 'hello'
        assert hasattr(x,'check')   #hasattr() 函数用于判断对象是否包含对应的属性

    def test_three(self):
        a='hello'
        b='hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main()