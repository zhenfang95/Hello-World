#!/usr/bin/env python

'''Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。'''

dict_1 = {"ww":"123","vbn":"njimko","qpoeqpo":"vmnvnvn"}
print(dict_1.items())

for key,value in dict_1.items():
    print(key,value)

#反转字典的key和value
#方法一
dict_2 = {y:k for k,y in dict_1.items()}
print(dict_2)
#方法二
dict_3 = dict(zip(dict_1.values(),dict_1.keys()))
print(dict_3)