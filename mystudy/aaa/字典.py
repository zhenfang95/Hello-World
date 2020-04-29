#!/usr/bin/env python

'''Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。'''

dict={"ww":"123","vbn":"njimko","qpoeqpo":"vmnvnvn"}
print(dict.items())

for key,value in dict.items():
    print(key,value)