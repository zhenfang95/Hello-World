#!/usr/bin/env python 
#coding:utf-8
from selenium import webdriver
import time
dr = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
dr.get("https://www.baidu.com")
time.sleep(2)
dr.find_element_by_id("kw").send_keys("博客")
#获取百度输入框的
time.sleep(2)
bd=dr.find_element_by_class_name("bdsug-overflow")
for i in bd:
    h = i.get_attribute("data-key")  #通过get_attribute()方法获取到文本信息
    print(h)
    if len(bd)>1:
        bd[1].click()
        print(dr.current_url)  #打印当前页面url
    else:
        print("未获取到匹配的词")