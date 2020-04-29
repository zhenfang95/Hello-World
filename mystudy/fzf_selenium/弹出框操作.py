#coding:utf-8
"""
text：获取文本值
accept() ：点击"确认"
dismiss() ：点击"取消"或者叉掉对话框
send_keys() ：输入文本值
"""
from selenium import webdriver
import time
url = "file:///E:/data/pythontestdata/python37/111.html"
driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.get(url)
time.sleep(2)
driver.find_element_by_id("alert").click()
time.sleep(3)
#用switch_to_alert()方法切换到alert弹出框上
t = driver.switch_to.alert
#打印alert框文本内容 ,用text方法获取弹出的文本 信息
print(t.text)
#点击alert框确认按钮,accept()点击确认按钮
t.accept()
#dismiss()相当于点右上角x，取消弹出框
#t.dismiss()

time.sleep(2)
driver.find_element_by_id("confirm").click()
time.sleep(3)
t1 = driver.switch_to.alert
print(t1.text)
#t1.accept()   #点击确定按钮
t1.dismiss()  #点击取消按钮

time.sleep(2)
driver.find_element_by_id("prompt").click()
time.sleep(3)
t2 = driver.switch_to.alert
print(t2.text)
#在弹窗的【输入框】中输入文本值
t2.send_keys("fuzhenfang")
time.sleep(2)
t.accept()
# t.dismiss()
