#!/usr/bin/env python 
#coding:utf-8
from selenium import webdriver
import time

def xzdz():
    driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
    driver.get("https://www.12306.cn/index/index.html")
    driver.find_element_by_id("fromStationText").clear()
    driver.find_element_by_id("fromStationText").send_keys("深圳")
    time.sleep(2)
    driver.find_element_by_id("toStationText").clear()
    driver.find_element_by_id("toStationText").send_keys("广州")
    time.sleep(2)
    #去掉元素的readonly属性，只有去掉readonly属性才能输入日期
    js = 'document.getElementById("train_date").removeAttribute("readonly");'
    driver.execute_script(js)  #执行js脚本
    driver.find_element_by_id("train_date").clear()
    driver.find_element_by_id("train_date").send_keys("2019-06-05")
    time.sleep(2)
    driver.find_element_by_id("search_one").click()
    time.sleep(2)
def aaa():
    driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
    driver.find_element_by_xpath("/html/body/div[7]/div[7]/table/tbody/tr/td[13]/a").click()

xzdz()
aaa()