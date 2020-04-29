print("%s is number %d" % ("python",1))
'''
logfile = open("E:/1.log","a")
print("hello world") >> logfile
'''

try:                           #尝试下面这个事
    file = open('eeee','r+')
except Exception as e:          #上面的如果有意外发生，执行下面这一段
    print('没有名为eeee的文件')
    response = input('你要创建新文件吗')
    if response=='y':
        file = open('eeee','w')
    else:
        pass
else:                          #没有意外，顺利执行，执行这一段
    file.write('没有不可能，只有不愿意')       #写入内容
    print('写入成功')

file.close()        #关闭文件

a = int
a = "1289"
print(a[::-1])


