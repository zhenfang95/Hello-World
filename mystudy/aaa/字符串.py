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

