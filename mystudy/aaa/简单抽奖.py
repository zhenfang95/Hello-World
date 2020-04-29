#coding:utf-8

import random
a = int(input('请输入抽奖号码：')) #int--通常被称为是整型或整数,是正或负整数,不带小数点
print('你的抽奖号码：',a)

#b = random.choice(range(100))     #从0，100随机取整数
b = random.randint(1000,9999)      #从1000到9999随机取整数
print('本期开奖号码：',b)

def abc():
    if a == b:
        return '恭喜中奖'           #return返回输出结果
    else:
        return '很遗憾，未中奖'
w = abc()
print(w)