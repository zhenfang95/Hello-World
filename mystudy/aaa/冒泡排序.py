#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/6/9 16:44
# @author:AlexFu

list1 = [21,6,1,0,2,44,34,12,67,98,7,9,3,43]

for i in range(len(list1)-1):
    for j in range(len(list1)-1-i):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]

print(list1)