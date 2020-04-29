#coding:utf-8
import requests
import urllib3
#禁用安全请求警告
urllib3.disable_warnings()
url = "https://passport.cnblogs.com/user/signin"
headers ={"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
# requests的请求默认verify=True,如果将verify设置为False，requests也能忽略对SSL证书的验证
r = requests.get(url,headers=headers,verify=False)
print(r.status_code)
print(r.text)