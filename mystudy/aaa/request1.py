#coding:utf-8
import requests
'''
requests模块发送请求有data、params两种携带参数的方法
params是把参数加到url后面，只在get请求时使用
data在post请求中使用
'''
'''
mydata = {"Username":"jojo","Password":"bean"}
r = requests.post("http://127.0.0.1:1080/WebTours/",data=mydata)
result = r.status_code
result1 = r.content     #输出返回信息content-type,josn格式
print(result,result1)
'''
r = requests.get("http://httpbin.org/get")
payload = {"key":"value1","key2":"value2","key3":None}
r = requests.get("http://httpbin.org/get",params=payload)
rr = r.status_code
rrr = r.text
print(rr,rrr)