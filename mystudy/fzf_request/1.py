#coding:utf-8
import urllib.request
import http.cookiejar
#创建一个cookiejar对象
cj = http.cookiejar.CookieJar()
#通过cookiejar创建一个handler
handler = urllib.request.HTTPCookieProcessor(cj)
#根据handler创建一个opener
opener = urllib.request.build_opener(handler)
'''所有请求操作都用opener.open()方法去发送请求，这里会带着cookie请求'''
