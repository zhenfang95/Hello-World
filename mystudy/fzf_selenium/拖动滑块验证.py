#!/usr/bin/env python 

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Firefox()
driver.get("http://passport.com.juooo.net.cn/User/register")
driver.implicitly_wait(5)
#定位滑块元素
source=driver.find_element_by_xpath("/html/body/div[2]/div/div/form[1]/div[5]/div/div/div/span[1]")
#实例化一个action对象
action=ActionChains(driver)
#action.click_and_hold(source).perform()   #鼠标左键按下不放
#action.move_by_offset(298,0).perform() #移动滑块
action.drag_and_drop_by_offset(source,300,0).perform()
#action.release().perform()   #释放鼠标
time.sleep(3)
driver.quit()


'''验证不成功时，重复验证直到成功为止'''
# driver=webdriver.Firefox()
# driver.get("https://reg.taobao.com/member/reg/fill_mobile.htm")
# driver.implicitly_wait(5)
# driver.find_element_by_id("J_AgreementBtn").click()
# time.sleep(2)
# while True:
#     try:
#         button=driver.find_element_by_id("nc_1_n1z")
#         ActionChains(driver).drag_and_drop_by_offset(button,258,0).perform()
#         time.sleep(2)
#         text=driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
#         if text.text.startswith("请在下方"):
#             print("成功滑动")
#             break
#         elif text.text.startswith("请点击"):
#             print("成功滑动")
#             break
#         elif text.text.startswith("请按住"):
#             continue
#     except Exception as e:
#         driver.find_element_by_xpath("//div[@id='register_no_captcha']/div/span/a").click()
#         print(e)


