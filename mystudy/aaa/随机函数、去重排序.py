#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/30 15:19

import random

s ='ABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789'
ran = random.sample(s,6)
aa ="".join(ran)
print(aa)

'''字符串去重并排序'''
w = "11235672asdwaaswvbg"
ww = list(set(w)) #去重
ww.sort()  #列表排序
wwww = "".join(ww)  #列表转换为字符
print(wwww)

