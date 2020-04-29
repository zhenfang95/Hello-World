#coding:utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.get("https://www.baidu.com")
#css通过id属性定位
driver.find_element_by_css_selector("#kw").send_keys("python")
#css通过class属性定位
driver.find_element_by_css_selector(".s_ipt").send_keys("是")
#css通过标签属性定位
#driver.find_element_by_css_selector("input").send_keys("python")
#css通过name属性定位
driver.find_element_by_css_selector("[name='wd']").send_keys("世界")
#css通过type属性定位
#driver.find_element_by_css_selector("[type='text']").send_keys("界")
#css通过标签与class属性的组合定位
driver.find_element_by_css_selector("input.s_ipt").send_keys("上")
#css通过标签与id属性的组合定位
driver.find_element_by_css_selector("input#kw").send_keys("最")
#css通过标签与其他属性的组合定位
driver.find_element_by_css_selector("input[id='kw']").send_keys("好")
#css通过层级关系定位
driver.find_element_by_css_selector("form#form>span>input").send_keys("的")
driver.find_element_by_css_selector("form.fm>span>input").send_keys("语言")  #fm 是该行class的值“class=fm”