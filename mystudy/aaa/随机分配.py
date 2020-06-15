#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/6/9 16:07
# @author:AlexFu

#pop()：移除序列中的一个元素（默认最后一个元素），并且返回该元素的值
#popitem()方法随机返回并删除字典中的一对键和值
dictGiftIn = {'Jack': 'apple', 'Peter': 'beer', 'Tom': 'card', 'Duke': 'doll', 'Mary': 'pineapple', 'James': 'flute',
              'Tina': 'coffee'}
dictGiftOut = {}
persons = list(dictGiftIn.keys())
for p in persons:
    flag = 0  # 标记自己带来的礼物是否还未分配出去
    if p in dictGiftIn:
        flag = 1
        myGift = dictGiftIn.pop(p)  # 如果自己带来的礼物还未分配，则去掉该礼物，通过key值去掉礼物并返回value值
    getGift = dictGiftIn.popitem()  # 随机返回并移除一对key-value值
    dictGiftOut[p] = getGift[1]  # 得到的礼物
    if flag:
        dictGiftIn[p] = myGift  # 将自己的礼物添到未分配礼物中

print(dictGiftOut)  # 输出礼物分配情况

