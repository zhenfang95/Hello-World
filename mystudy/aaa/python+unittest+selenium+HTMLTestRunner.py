#coding: utf-8 
import unittest
import time
from selenium import webdriver
import os
import requests
import HTMLTestRunner

import sys
sys.path.append("D:\PycharmProjects\FmjTest\Base")# 由于自定义模块和执行文件不在同一个路径下，所以要单独指定使用append。
#import HttpRequest

#reload(sys)  # 一次性修改程序或系统的默认编码，重新加载sys这个模块
#sys.setdefaultencoding("utf-8")  # 默认的编码是ascii，设置默认编码时使用utf-8

# 测试用例
class demoTest(unittest.TestCase):
    u'''这只是一个例子'''
    def setUp(self):
        self.Http = requests.Http("http://www.baidu.com/")
        # 返回文件路径
        self.data_file = os.path.split(os.path.realpath(__file__))[0]
        self.class_name = self.__class__.__name__
        super(demoTest, self).setUp()
        
    def test_httpBaidu(self):
        u'''以百度为例作为测试'''
        content = self.Http.Get("http://www.baidu.com/", is_json = False)
        self.assertEqual(content, 200)
        
    def test_add(self):
        u'''加法的测试'''
        content = 4 + 5
        self.assertEqual(content, 8)
        
    def test_Ui(self):
        u'''UI的测试，同时生成报告和图片'''
        executable_path = r'C:\Users\fmj\AppData\Local\Google\Chrome\Application\chromedriver.exe'
        driver = webdriver.Chrome(executable_path)
        driver.get("http://www.baidu.com")
        driver.get_screenshot_as_file(path + "login_success.jpg")
        
        print(driver.title)
        self.assertEqual(driver.title, u'百度一下，你就知道')
        time.sleep(3)
        driver.close()
      
# 主函数
if  __name__ == '__main__':
    # 构造测试集
    testSuite = unittest.TestSuite()
    testSuite.addTest(demoTest('test_httpBaidu'))
    testSuite.addTest(demoTest('test_add'))
    testSuite.addTest(demoTest('test_Userinterface'))
    
    # 定义测试报告的地址
    path = 'D:\\PycharmProjects\\FmjTest\\result\\'
    report_path = path + 'result.html'
    
    # 如果路径不存在，创建路径
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass
    fp = file(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title= u'网管子系统Http接口测试报告', description='Report_description')
    
    # 执行测试
    runner.run(testSuite)