#coding:utf-8
import requests
# 禅道登录地址
host = "http://zt.juooo.cn:8090/www/index.php?m=user&f=login"
def login(s,username,psw):
    url = host
    h = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Referer": host,
        # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        }

    body1 = {"account": username,
             "password": psw,
             "keepLogin[]": "on",
             "referer":"http://zt.juooo.cn:8090/www/index.php?m=bug&f=browse&productid=32&branch=0&browseType=assigntome&param=0"
            }

    # s = requests.session()   不要写死session

    r1 = s.post(url,data=body1,headers=h)
    # return r1.content  # python2的return这个
    return r1.content.decode("utf-8")  # python3

def is_login_sucess(res):
        if "登录失败，请检查您的用户名或密码是否填写正确。" in res:
                return False
        elif "parent.location=" in res:
                return True
        else:
                return False

if __name__ == "__main__":
    s = requests.session()
    a = login(s, "fuzhenfang", "465b66a0e03680206126e04fe638c0ba")
    result = is_login_sucess(a)
    print("测试结果：%s"%result)