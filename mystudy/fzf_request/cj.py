#coding:utf-8

import urllib.request
import urllib.parse
import http.cookiejar

#创建cookie实例对象
ck = http.cookiejar.CookieJar()
#根据创建的cookie生成cookie的管理器
ck_handle = urllib.request.HTTPCookieProcessor(ck)
#创建http请求管理器
http_handle = urllib.request.HTTPHandler()
#创建https管理器
https_handle = urllib.request.HTTPSHandler()
#创建请求管理器，opener替代urlopen来获取请求
opener = urllib.request.build_opener(ck_handle,http_handle,https_handle)

def login():
    '''第一次登陆需要传递用户名和密码，来获取登陆的cookie凭证'''
    url = "http://zt.juooo.cn:8090/www/index.php?m=user&f=login"
    paydata={'account':'fuzhenfang',
                'keepLogin[]':'on',
                'password':'fa5490fcf84f45110ae6e61df0a0b3a7',
                'referer':"http://zt.juooo.cn:8090/www/index.php?m=my&f=index"
                }
    #将数据解析成urlencode格式,将str类型转换为bytes类型
    cod_data = urllib.parse.urlencode(paydata).encode("utf-8")
    r = urllib.request.Request(url,data=cod_data)
    #用opener.open()发起请求
    response = opener.open(r)
    return response

def gethome():
    '''获取登陆后的页面'''
    #登陆后的地址
    url = "http://zt.juooo.cn:8090/www/index.php?m=my&f=index"
    #如果执行了login()函数，则此时的opener已经包含了cookie信息的一个opener对象
    r = opener.open(url)
    html = r.read().decode()
    print(html)
    #生成html文件
    with open("jucheng.html","w",encoding="utf-8") as f:
        f.write(html)

if __name__=="__main__":
    login()
    gethome()



