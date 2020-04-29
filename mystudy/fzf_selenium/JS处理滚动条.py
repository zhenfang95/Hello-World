#coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.get("http://www.juooo.com/")
#获取浏览器名称，然后用if语句作判断
bowser = driver.name
#拉到顶部
def scroll_top():
    if bowser == "chrome":
        js = "var q=document.body.scrollTop=0"     #js脚本
    else:
        js = "var q=document.documentElement.scrollTop=0"
    return driver.execute_script(js)
#拉到底部
def scroll_foot():
    if bowser == "chrome":
        js = "var q=document.body.scrollTop=10000"
    else:
        js = "var q=document.documentElement.scrollTop=10000"
    return driver.execute_script(js)
s=scroll_top()
print(s)
s1=scroll_foot()
print(s1)

#滚动到底部
js = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
time.sleep(2)
#滚动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)
time.sleep(2)

#聚焦元素
#target = driver.find_element_by_xxxx()
#driver.execute_script("arguments[0].scrollIntoView();", target)

# 横向滚动条
# 通过左边控制横向和纵向滚动条scrollTo(x, y）js = "window.scrollTo(100,400);"