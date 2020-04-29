#!/usr/bin/env python 
from selenium import webdriver
import pytest

driver=None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """当测试失败的时候，自动截图，展示到html报告中"""
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield     #执行teardown()
    report = outcome.get_result()
    extra = getattr(report,'extra',[]) #getattr() 函数用于返回一个对象属性值
    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report,'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::","_")+".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'% screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot():
    '''截图保存为base64,展示到html中'''
    return driver.get_screenshot_as_base64()

@pytest.fixture(scope='session',autouse=True)
def browser():
    global driver  #global 属性用于返回正则表达式是否具有 "g" ,如果 g 标志被设置，则该属性为 true，否则为 false
    if driver is None:
        driver = webdriver.Firefox()
    return driver
