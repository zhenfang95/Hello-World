#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/9/16 10:51

class ExcelVariable:
    caseID = 1
    caseName = 2
    method = 3
    data = 4
    expect = 5
    result = 6
    my_sql = 7

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

