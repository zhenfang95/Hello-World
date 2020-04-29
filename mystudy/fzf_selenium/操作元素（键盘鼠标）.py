#coding:utf-8
from selenium import webdriver
import time
#模拟键盘操作要先导入键盘模块
from selenium.webdriver.common.keys import Keys
#模拟鼠标事件需要先导入鼠标模块
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.get("http://www.testerhorde.com")
driver.implicitly_wait(5)
driver.find_element_by_id("search-button").click()
driver.find_element_by_id("search-term").clear()
driver.find_element_by_id("search-term").send_keys("selenium")
time.sleep(2)
#模拟回车键操作回车按钮
driver.find_element_by_id("search-term").send_keys(Keys.ENTER)
#鼠标悬停在按钮上
mouse = driver.find_element_by_link_text("分享")
ActionChains(driver).move_to_element(mouse).perform()
"""
键盘F1到F12：send_keys(Keys.F1) 把F1改成对应的快捷键
复制Ctrl+C：send_keys(Keys.CONTROL,'c') 
粘贴Ctrl+V：send_keys(Keys.CONTROL,'v') 
全选Ctrl+A：send_keys(Keys.CONTROL,'a') 
剪切Ctrl+X：send_keys(Keys.CONTROL,'x') 
制表键Tab:  send_keys(Keys.TAB) 
"""

