#!/usr/bin/env python

import time

def test_01(browser):    #直接继承browser方法
    browser.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(2)
    t = browser.title
    assert t == "上海-悠悠"

