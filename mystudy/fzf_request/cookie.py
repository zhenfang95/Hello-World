#!/usr/bin/env python
import requests
import json
import re
def login():
    '''登录'''
    pydata={'username':'15217043402','password':'fzf123456','loginType':3}
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    url='http://passport.com.juooo.net.cn/User/doLoginRoute'
    s=requests.session()
    r=s.post(url,headers=headers,data=pydata)
    #获取登录响应头中的cookie，并以json格式输出
    cookie=r.cookies
    cook=requests.utils.dict_from_cookiejar(cookie)
    return cook

def opendoor():
    '''进入个人中心'''
    cookies=login()
    pydata={'type':5}
    r=requests.post('http://myjuooo.com.juooo.net.cn/User/opendoor',data=pydata,cookies=cookies)
    c=r.content.decode('utf-8')
    j=json.loads(c)    #反序列化
    #k=re.findall(r'code":(.+?)',c)     #正则表达式提取数据
    return j

print(opendoor())
