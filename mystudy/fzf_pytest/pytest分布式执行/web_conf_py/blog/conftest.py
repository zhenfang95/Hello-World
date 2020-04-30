#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/4/30 16:48
# @author:AlexFu

import pytest

@pytest.fixture(scope="function")
def open_blog():
    print("打开blog页面_function")

