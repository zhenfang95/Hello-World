#!/usr/bin/env python 
#coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.get("http://sh.xsjedu.org/")
time.sleep(2)
#将display的值设置成none就可以去除这个弹窗
js = 'document.getElementById("doyoo_monitor").style.display="none"'
driver.execute_script(js)