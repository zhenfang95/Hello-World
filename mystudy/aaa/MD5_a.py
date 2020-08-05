#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/5 11:03

import hashlib

a = '123456789'
s = a.encode() #转换为bytes类型
ss = hashlib.md5(s)
print(ss.hexdigest())

def Md5(str1):
    m = hashlib.md5(str1.encode())
    return m.hexdigest()

