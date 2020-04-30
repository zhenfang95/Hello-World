#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/4/30 16:40
# @author:AlexFu

import pytest

@pytest.fixture(scope='session')
def open_baidu():
    print('打开百度页面_session')
