#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/7/26 17:13

import yaml
from common import pubilc

def getSele(title='login',name=None):
    '''读取yaml数据'''
    path = pubilc.get_cwd()
    readfeil = open(path+'\\data\\sele_data.yaml','r',encoding='utf-8')
    dict1 = yaml.load(readfeil,Loader=yaml.FullLoader)
    data = dict1[title].get(name)
    return data

def getTest(title,name):
    path = pubilc.get_cwd()
    readfeil = open(path+'\\data\\testData.yaml','r',encoding='utf-8')
    dict1 = yaml.load(readfeil,Loader=yaml.FullLoader)
    data = dict1[title].get(name)
    return data
