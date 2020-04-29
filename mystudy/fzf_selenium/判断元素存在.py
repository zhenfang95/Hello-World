#!/usr/bin/env python 
#coding:utf-8

from selenium import webdriver

driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#写一个函数判断，找到就返回Ture.没找到就返回False
def is_element_exist(css):
    s = driver.find_elements_by_css_selector(css_selector=css)
    if len(s) == 0:
        print("元素未找到：%s" %css)
        return False
    elif len(s)== 1:
        return True
    else:
        print("找到%s个元素：%s" %(len(s),css))
        return False
# 判断页面有无id为kw的元素
if is_element_exist("#kw"):
    driver.find_element_by_id("kw").send_keys("NBA")
# 判断页面有无标签为input的元素
if is_element_exist("input"):
    driver.find_element_by_tag_name("input").send_keys("NBA")
# 判断页面有无id为xxx的元素
if is_element_exist("xxx"):
    driver.find_element_by_id("xxx").send_keys("NBA")

#捕获异常
def isElemenExist(css):
    try:
        driver.find_element_by_css_selector(css)
        return True
    except:
        return False

is_element_exist("kw")
print(isElemenExist("kw"))