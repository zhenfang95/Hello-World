#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/21 16:34

import pytest,allure,requests,json
from case.conftest import *
from common.readExcel import OperationExcel
from common.readYaml import *
from common.reData import *

ml = OperationExcel()

@allure.feature('01、登录模块')   #在报告中添加用例标题
class TestDemo:
    @pytest.mark.parametrize('row',row(),ids=caseName())   #ids是增加用例标题
    def testDemo(self,row):
        '''登录用例验证'''
        r = requests.post(url=getFixedData(key1='url01'),data=ml.getRequestData(row))
        print(r.text)
        assert ml.getExpect(row) in r.text

if __name__ == '__main__':
    pytest.main(['-s','-v','test_001.py::TestDemo'])
    # 执行：pytest --alluredir ./report/allure_raw
    # 打开报告：allure serve report/allure_raw