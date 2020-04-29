#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains      #导入鼠标模拟模块
from selenium.webdriver.support.select import Select          #导入select模块(index)
driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(5)
#鼠标移动到“设置”按钮
mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()

# 分两步：先定位下拉框，再点击选项
# s = driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='50']").click()

#直接定位
# driver.find_element_by_xpath(".//*[@id='nr']/option[2]").click()

#通过索引：select_by_index()
#s = driver.find_element_by_id("nr")
#Select(s).select_by_index(2)

#通过值value：select_by_value()
#s = driver.find_element_by_id("nr")
#Select(s).select_by_value("20")

"""
select_by_visible_text() :通过文本值定位
deselect_all()          ：取消所有选项
deselect_by_index()     ：取消对应index选项
deselect_by_value()      ：取消对应value选项
deselect_by_visible_text() ：取消对应文本选项
first_selected_option()  ：返回第一个选项
all_selected_options()   ：返回所有的选项 
"""