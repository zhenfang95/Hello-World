#修改、添加和删除元素
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])      #返回最后一个元素
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

motor = ['hello','yamaha','suzuki']
print(motor)
motor[1] = 'world'    #修改列表元素
print(motor)
motor.append("你好")   #在列表后面增加元素
print(motor)
motor.insert(1,"我好")  #在列表任何位置添加元素
print(motor)

del motor[1]     #删除元素
print(motor)

motor.pop()  #删除列表末尾元素
print(motor)
a = motor.pop(0)  #取出列表中的元素，不写元素位置默认取出末尾元素
print(a)

#组织列表
#sort()对列表进行永久性排序
cars = ['bmw','aodi','toyota','subaru']
cars.sort()    #按首字母顺序排序
print(cars)
#reverse=True 按首字母顺序相反的顺序排列元素
cars.sort(reverse=True)
print(cars)
#reverse=False 按首字母顺序排列元素
cars.sort(reverse=False)
print(cars)

#sorted()对列表进行临时排序
cars1 = ['ymw','codi','foyota','bubaru']
print(sorted(cars1))
print(cars1)

#reverse() 反转列表元素的排列顺序
cars2 = ['ymw','codi','foyota','bubaru']
cars2.reverse()
print(cars2)

#len() 获取列表长度
a = len(cars2)
print(a)


mags = ['alice','david','carolina']
for mag in mags:       #从列表中依次取出元素
    pass               #pass是站位符，没啥作用
    if len(mag)>1:
        print(mag.title() + ",that was a great trick!")
        print("I can't wait to see your next trick," + mag.title() + ".\n") #\n 换行符，在每次迭代结束后都插入一个空行
    else:
        print("谢谢")
print("Thank you, everyone. That was a great magic show!")

numbers = list(range(1,10))
print(numbers)
e_numbers = list(range(1,11,2)) #指定步长2
print(e_numbers)

a = [0,1,2,3,4,5,6,7,8,9]
print(max(a))
print(min(a))
print(sum(a))

print(a[1:3])           #切片
print(mags[0:1])
print(a[::-1])  #倒序排序
print(a[-1])  #取最后一位
print(a[-3:-1])  #从后面开始取值

b = [1,5,3,22,33,5,1,4,7,4]
#去重
bb=list(set(b))
bb.sort()  #从小到大排序
print(bb)
#从小到大排序
b.sort()  #方法二
print(b)
#拼接
print(a+b)