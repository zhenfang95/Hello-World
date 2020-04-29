#coding:utf-8
import unittest
from selenium import webdriver
import time

driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
time.sleep(2)
driver.get("https://www.baidu.com")
#浏览器窗口最大化
#driver.maximize_window()
#等待元素加载时间5s
driver.implicitly_wait(5)
"""driver.get("http://www.juooo.com/")
time.sleep(2)
# 返回上一页面
driver.back() 
time.sleep(2)
#切换到下一页面
driver.forward()    
time.sleep(2)
#截屏+保存路径
driver.get_screenshot_as_file("E:\\tsetdate\\b1.png")   
# 刷新页面
driver.refresh() 
time.sleep(2)
"""
"""
1、点击（鼠标左键）页面按钮：click()
2、请空输入框：clear()
3、输入字符串：send_keys()
"""
driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("测试论坛")
#submit()模拟回车键提交表单
driver.find_element_by_id("kw").submit()

#driver.close()    #关闭当前窗口
#driver.quit()     #退出浏览器
