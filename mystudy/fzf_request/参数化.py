#coding:utf-8
import requests

def login(s,url,paydata):
    '''登录'''
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    r = s.post(url,headers=headers,data=paydata)
    result = r.json()
    print(result)
    return result
if __name__=="__main__":
    s =requests.session()
    url = "http://passport.juooot.com/User/doLoginRoute"
    paydata = {"username":"13097888019","password":"123456","loginType":"3"}
    login(s,url,paydata)