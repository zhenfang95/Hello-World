#coding:utf-8
"""
frame和iframe区别:
Frame与Iframe两者可以实现的功能基本相同，不过Iframe比Frame具有更多的灵活性。
frame是整个页面的框架，iframe是内嵌的网页元素，也可以说是内嵌的框架
"""
from selenium import webdriver
import time

driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.get("https://mail.163.com/")
driver.implicitly_wait(5)
#跳出所有frame框架
driver.switch_to.default_content()
#切换到iframe框架
#driver.switch_to.frame("x-URS-iframe1557390566496.1997")
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)
#定位元素
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("13097888019")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("fzf19951208")
driver.find_element_by_id("dologin").click()
