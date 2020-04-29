wo_name ="alex"
motto_name = "no impossible, only unwilling"
wo_motto =wo_name+" : "+motto_name
print("hello",wo_motto.title() + "!")

ww = "Albert Einstein once said,'A person who never made a mistake never tried anything new.'"
print(ww)
famous_person = "Alex"
message = famous_person + ":\n\t" + ww
print(message)

pa = ['榴莲','鸡肉','烤肉','沙拉']
for p in pa:
    print("披萨的味道：",p)

for i in range(1,21):
    print(i)
print(list(range(20)))

a = list(range(1,100,2))
print(sum(a))
print(a)

a1 = [w**2 for w in range(1,11)] #平方数列表
print(a1)