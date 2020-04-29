#coding:utf-8
import urllib.request
#构造并返回一个request对象
request  = urllib.request.Request("https://www.baidu.com/")
#发送给服务器并接受响应
response = urllib.request.urlopen(request)
h = response.read()
print(h)
