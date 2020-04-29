#!/usr/bin/env python 

'''
eval()函数是实现list、dict、tuple、与str之间的专化
str函数把list、dict、tuple转为字符串
'''
#字符串转换成列表
#a="[[1,2], [3,4], [5,6], [7,8], [9,0]]"
a="['w', 'e', 'r', 'qq', 'a']"
print(type(a))
b=eval(a)
print(type(b))
print(b)

#字符串转换成字典
a1="{'name':'fzf','age':20}"
print(type(a1))
b1=eval(a1)
print(type(b1))
print(b1)

#字符串转换成元组
# a2="('你','好','深','圳')"
a2="(1,2,3,4,5,6,7,8,9)"
print(type(a2))
b2=eval(a2)
print(type(b2))
print(b2)

