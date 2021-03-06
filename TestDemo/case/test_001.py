#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/21 16:34

import pytest,allure,requests,json
from common.readExcel import OperationExcel
from common import readYaml,readMySQL,reData

ml = OperationExcel()
dt = reData
yl = readYaml
db = readMySQL

@allure.feature('01、登录模块')   #在报告中添加用例标题
class TestDemo:
    @pytest.mark.parametrize('row',dt.row(),ids=dt.caseName())   #ids是增加用例标题
    def testDemo(self,row):
        '''登录用例验证'''
        if ml.getSql(row) == None:
            r = requests.post(url=yl.getFixedData(key1='url01'),data=ml.getRequestData(row))
            print(r.text)
            assert ml.getExpect(row) in r.text
        else:
            r = requests.post(url=yl.getFixedData(key1='url01'),data=ml.getRequestData(row))
            print(r.text)
            assert db.Mysql(ml.getSql(row)) in r.text

if __name__ == '__main__':
    pytest.main(['-s','-v','test_001.py::TestDemo'])


# 执行：pytest --alluredir ./report/allure_raw
# 打开报告：allure serve report/allure_raw