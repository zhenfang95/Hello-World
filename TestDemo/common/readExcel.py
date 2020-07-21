#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/9/16 10:01

import xlrd,os
from common.excel_data import *

class OperationExcel:
    def __init__(self):
        self.data = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data','xiaoeTest.xls')

    def getExcel(self):
        db = xlrd.open_workbook(self.data)
        sheet = db.sheet_by_index(0)
        return sheet

    def getRows(self):
        '''获取行数'''
        return self.getExcel().nrows

    def getCell(self,row,col):
        '''获取文件内容'''
        return self.getExcel().cell_value(row,col)

    def getCaseID(self,row):
        '''获取caseid'''
        return self.getCell(row,getCaseID())

    def getCaseName(self,row):
        '''获取用例名称'''
        return self.getCell(row,getCaseName())

    def getMethod(self,row):
        '''获取请求方式'''
        return self.getCell(row,getMethod())

    def getRequestData(self,row):
        '''获取请求参数'''
        return self.getCell(row,getRequest_Data())

    def getExpect(self,row):
        '''获取预期结果'''
        return self.getCell(row,getExpect())

    def getResult(self,row):
        '''获取实际结果'''
        return self.getCell(row,getResult())

    def getSql(self,row):
        '''获取sql'''
        return self.getCell(row,getSql())

