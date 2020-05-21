#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/5/21 10:03
# @author:AlexFu

import redis

#连接redis
r = redis.Redis(host='192.168.231.128',port=6379,password='123456')
#添加数据（key，value）
r.set('haha','kaka')
#通过key值获取数据
d = r.get('haha')
print(d)

