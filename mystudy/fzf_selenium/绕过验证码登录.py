#!/usr/bin/env python 
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://myjuooo.com.juooo.net.cn/User/myorderlist")
#print(driver.get_cookies())  #获取cookie

#添加cookie
c1 = {'name':'juooo_sessionid',
      'value':'gucacmiccc0hf12j0epos1vj05',
      'path': '/',
      'domain': '.juooo.net.cn',
      'secure': False,
      'httpOnly': False}

c2 = {'name':'juooo_sessionid',
      'value':'gucacmiccc0hf12j0epos1vj05',
      'path': '/',
      'domain': '.juooo.net.cn',
      'secure': False,
      'httpOnly': False}

#添加cookie值
driver.add_cookie(c1)
driver.add_cookie(c2)
time.sleep(2)

#刷新页面
driver.refresh()