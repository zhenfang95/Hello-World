#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/4/30 15:31
# @author:AlexFu

import pytest

@pytest.fixture()
def fzf1():
    a = '没有不可能'
    return a

@pytest.fixture()
def fzf2():
    b = '只有不愿意'
    return b

def test1(fzf1,fzf2):
    x = fzf1
    y = fzf2
    assert x == '没有不可能'
    assert y == '只有不愿意'
    print(x,y)

if __name__ == '__main__':
    pytest.main()