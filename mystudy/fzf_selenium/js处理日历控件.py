#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.get("https://www.12306.cn/index/index.html")

#去掉元素的readonly属性，只有去掉readonly属性才能输入日期
js = 'document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)  #执行js脚本

#清空后输入日期
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2019-07-04")

#用js方法输入日期
# js_value = 'document.getElementById("train_date").value="2019-12-25";'
# driver.execute_script(js_value)

time.sleep(3)
driver.quit()