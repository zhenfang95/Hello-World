#合并（拼接）字符串

first_name = "ada"
last_name = "lovelace"
print(first_name+last_name)
full_name = first_name + " " +last_name
print(full_name)
print("hello," + full_name.title()+"!")  #title()将姓名设置为合适的格式，首字母大写
message = "hello," + full_name.title() + "?"
print(message)

#转义符号
#换行符 \n
print("Languages:\nPython\nC\nJavaScript")
#制表符 \t  缩进4个字符
print("Languages:\n\tPython\n\tC\n\tJavaScript")
print(r"Languages:\n\tPython\n\tC\n\tJavaScript")  # r 表示不执行转义符，使字符串中的转义符号失效

#删除空白
favorite_language = " python "
f = favorite_language.rstrip()  #rstrip()删除字符串尾端的空白
print(f)
t = favorite_language.lstrip()  #lstrip()删除字符串开头的空白
print(t)
k = favorite_language.strip()   #strip()同时删除字符串两端的空白
print(k)

a = "123asdd33"
print(a[0:3])
print(a[1::3]) #隔2位取值
print(a[::-1]) #倒序排列
print(a[-3:-1]) #取倒数第几的值
#去重
aa = list(set(a))
aa.sort() #排序
aaa = "".join(aa) #连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
print(aaa)

w = "dhjsa/dsdd/2321sda"
print(w.split("/")) #通过指定分隔符对字符串进行切片，转成列表格式

print(a.upper())