#coding:utf-8
#coding:utf-8
import requests
payload = {"username":"13097888019","password":"123456","loginType":"3"}
url ="http://passport.juooo.net.cn/User/doLoginRoute"
# headers是一个字典，不是字符串
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
s = requests.session()
r = s.post(url,headers=headers,data=payload,verify=False)
j = r.json()
print(j)