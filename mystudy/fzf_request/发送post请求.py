#coding:utf-8
import requests
import json
payload = {"username":"13097888019","password":"123456","loginType":"3"}
#用json参数传入
#data_json = json.dumps(payload)  #转化成json格式
r = requests.post("http://passport.juooot.com/User/doLoginRoute",data=payload)
c = r.status_code
j = r.json()
print(c,j)

'''import requests
from requests.cookies import RequestsCookieJar
url = "http://passport.juooo.net.cn/User/doLoginRoute"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
s = requests.session()
r = s.get(url,headers=headers)
w = r.cookies
print(w)
c = requests.cookies.RequestsCookieJar()
c.set("UM_distinctid","16a66e932e112b-0ad5b004fe426d-39395704-1fa400-16a66e932e23ecag_fid=7tKpfanIJ35GsiuF")
c.set("juooo_sessionid",w)
s.cookies.update(c)
print(r.cookies)
print(r.json())
'''