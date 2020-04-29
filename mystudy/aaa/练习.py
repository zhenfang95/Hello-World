#coding:utf-8

#计算数组中正整数的平均值
number =[2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]

# count=0
# sum=0
# for i in range(number):
#     if number[i]>0:
#         count +=1
#         sum += number[i]
#     if count>0:
#         avg = sum/count
#         print(avg)

a=sum([i for i in number if i>0])/len([i for i in number if i>0])
print(a)

count=0
sum = 0
for i in number:
    if i>0:
        sum=sum+i
        count += 1
if count>0:
    avg=sum/count
    print(avg)





def num():
    return [lambda x:i*x for i in range(4)]
print([m(2) for m in num()])

import time
print(time.time())

t=time.strftime('%Y-%m-%d %H:%M:%S')
print(t)


for i in range(1,10):
    for j in range(1,i+1):
        if i>=j:
            print('%d*%d=%-5d' %(i,j,i*j),end='')
    print()