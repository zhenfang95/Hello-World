#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/7/18 21:53

from common.readExcel import OperationExcel

def row():
    row1 = []
    for i in range(1,OperationExcel().getRows()):
        if OperationExcel().getResult(i) == 'Y':
            row1.append(i)
        else:
            pass
    return row1

def caseName():
    name = []
    for i in row():
        name.append(OperationExcel().getCaseName(i))
    return name

def my_sql():
    sql1 = []
    for i in row():
        sql1.append(OperationExcel().getSql(i))
    return sql1
