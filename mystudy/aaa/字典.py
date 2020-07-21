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


mydict = {0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖'}
mylist = ['拾', '佰', '仟', '万', '厘', '分', '角']
def dtym(je):
    aa = list(mydict.keys())
    b = list(je)
    if len(b) > 1:
        print(mydict[aa[b[0]]]+mylist[0]+mydict[aa[b[1]]])

dtym('12')