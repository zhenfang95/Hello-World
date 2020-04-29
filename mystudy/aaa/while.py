
count = 0
while count < 9:
    print("the count is:",count)
    count = count + 1
print("good bye")

num = []
i = 2
for i in range(2,100):
    j = 2
    for j in range(2,i):
        if (i%j == 0):
            break      #break语句用来终止循环语句，终止整个循环

        else:
            num.append(i)
print(num)


for letter in 'Python':  # 第一个实例
    if letter == 'h':
        break            #当满足if条件时就终止循环，执行下一行代码，break是跳出整个循环
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    print('当前变量值 :', var)
    var = var - 1
    if var == 5:  # 当变量 var 等于 5 时退出循环
        break

print("Good bye!")

for let1 in ["a","b","c","d","e"]:
    if let1 == "c":
        continue    #continue是跳出本次循环，继续执行下次循环
    print(let1)

var1 = 10
while var1 > 0:
    var1 = var1 -1
    if var1 == 4:
        continue
    print(var1)
print("Good bye!")


