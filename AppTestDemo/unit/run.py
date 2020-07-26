#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/7/26 17:58

import unittest,os
from common import pubilc, HTMLTestRunner

path=pubilc.get_cwd()
case_path=os.path.join(path,"case")

def run_case():
    #加载测试用例
    suite=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(start_dir=case_path,
                                                 pattern='test*.py',
                                                 top_level_dir=None)
    for test in discover:
        for test_case in test:
            suite.addTest(test_case)
    #当前时间
    #t = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
    #生成测试报告
    filename=os.path.join(path,'report','最新UI自动化测试报告.html')
    fp=open(filename,'wb')
    runner= HTMLTestRunner.HTMLTestRunner(stream=fp,
                                          verbosity=2,
                                          title='UI自动化测试报告',
                                          description='测试结果')
    runner.run(suite)

if __name__ == '__main__':
    run_case()