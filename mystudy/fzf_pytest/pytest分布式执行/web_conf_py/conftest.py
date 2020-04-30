#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/4/30 16:39
# @author:AlexFu

import pytest

@pytest.fixture(scope='session')
def start():
    print('\n打开首页')
    return 'yoyo'
