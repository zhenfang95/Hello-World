#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/9/16 10:51

class ExcelVariable:
    caseID = 0
    caseName = 1
    method = 2
    data = 3
    expect = 4
    result = 5
    my_sql = 6

def getCaseID():
    return ExcelVariable.caseID

def getCaseName():
    return ExcelVariable.caseName

def getMethod():
    return ExcelVariable.method

def getSql():
    return ExcelVariable.my_sql

def getRequest_Data():
    return ExcelVariable.data

def getExpect():
    return ExcelVariable.expect

def getResult():
    return ExcelVariable.result

