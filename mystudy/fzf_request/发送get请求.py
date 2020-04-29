#coding:utf-8
import requests
r = requests.get("http://www.juooo.com/")
s = r.status_code
c = r.cookies
t = r.text
print(s,"\n",c,"\n",t)
