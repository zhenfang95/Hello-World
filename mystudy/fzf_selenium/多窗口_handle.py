#coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.get("http://bj.ganji.com/")
driver.implicitly_wait(5)
#获取当前窗口句柄（handle）
h = driver.current_window_handle
print(h)  #打印首页句柄
driver.find_element_by_link_text("工作").click()
all_h = driver.window_handles
print(all_h) #打印所有的句柄

for i in all_h:
    if i != h:
        driver.switch_to.window(i)  #切换到i页面
        print(driver.title)         #获取当前页面的title

driver.close()  #关闭窗口
driver.switch_to.window(h)  #切换到首页
print(driver.title)
