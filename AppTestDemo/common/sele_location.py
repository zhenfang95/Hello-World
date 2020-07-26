#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/7/26 16:54

from appium import webdriver
from common.logs import log1

class PySele():
    def __init__(self):
        '''android固定参数设置'''
        desired_caps = {}  # 定义启动设备需要的参数
        desired_caps['platformName'] = 'Android'  # 设备的操作系统
        desired_caps['platformVersion'] = '5.1.1'  # 设备的系统版本号
        desired_caps['deviceName'] = '127.0.0.1:62001'  # 设备名称，使用手机类型或者模拟器类型
        desired_caps['appPackage'] = 'com.tencent.mobileqq'  # 要测试的应用的包名
        desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'  # 启动的activity参数
        # 默认使用appium自带输入法
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver=driver
        log1.info("打开待测APP")

    def element(self,fangfa,dingwei):
        '''元素定位'''
        if fangfa == 'id':
            element=self.driver.find_element_by_id(dingwei)
        elif fangfa == 'name':
            element=self.driver.find_element_by_name(dingwei)
        elif fangfa == 'class':
            element=self.driver.find_element_by_class_name(dingwei)
        elif fangfa == 'xpath':
            element=self.driver.find_element_by_xpath(dingwei)
        elif fangfa == 'link_text':
            element=self.driver.find_element_by_link_text(dingwei)
        elif fangfa == 'tag':
            element=self.driver.find_element_by_tag_name(dingwei)
        elif fangfa == 'css':
            element=self.driver.find_element_by_css_selector(dingwei)
        else:
            log1.error("没有找到元素")
            raise NameError("请输入定位元素方法,如'id','name','class','link_text','xpath','css','tag'")
        log1.info("元素定位成功，定位方法：%s，元素值：%s" %(fangfa,dingwei))
        return element

    def send_key(self, fangfa, dingwei, text):
        '''输入内容'''
        try:
            e1 = self.element(fangfa, dingwei)
            e1.clear()
            e1.send_keys(text)
            log1.info("输入的测试内容：%s" %text)
        except Exception as e:
            log1.error("输入测试内容异常，原因：%s" %e)

    def clear(self, fangfa, dingwei):
        '''清空'''
        e1 = self.element(fangfa, dingwei)
        e1.clear()
        log1.info("清空输入框内容")

    def click(self, fangfa, dingwei):
        '''点击'''
        try:
            e1 = self.element(fangfa, dingwei)
            e1.click()
            log1.info("点击元素成功")
        except Exception as e:
            log1.info("点击元素异常，原因：%s"%e)

    def click_text(self, text):
        '''点击文字'''
        self.driver.find_element_by_link_text(text).click()
        log1.info("点击文本内容:%s"%text)

    def close(self):
        '''关闭'''
        self.driver.close()
        log1.info("关闭app")

    def quit(self):
        '''退出'''
        self.driver.quit()
        log1.info("退出app")

    def js(self, sprit):
        '''执行js'''
        try:
            self.driver.execute_script(sprit)
            log1.info("执行js成功，js内容为：%s" %sprit)
        except Exception as e:
            log1.error("执行js报错，原因：%s" %e)


    def get_screen(self, file_path):
        '''截图'''
        try:
            self.driver.get_screenshot_as_file(file_path)
            log1.info("截图保存成功，保存路径为：%s" %file_path)
        except Exception as e:
            log1.error("截图失败，原因：%s" %e)

    def wait(self,s):
        '''等待'''
        self.driver.implicitly_wait(s)

    def asset(self, fangfa, dingwei):
        '''查找元素文本(断言用)'''
        try:
            self.element(fangfa, dingwei)
            e1=self.element(fangfa, dingwei).text
            log1.info("断言成功")
            return e1
        except Exception as e:
            log1.error("断言失败，原因：%s" %e)