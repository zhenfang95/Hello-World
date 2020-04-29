#coding:utf-8
import requests
# 请求头
headers = {
           "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
          }
s = requests.session()
# 打开我的随笔
r = s.get('https://i.cnblogs.com/EditPosts.aspx?opt=1',
          headers=headers,
          allow_redirects=False, #False是禁止重定向，True是启动重定向,
          verify=False)
# 打印状态码，自动处理重定向请求
print(r.status_code)
new_url = r.headers["Location"]   #获取重定向请求地址
print(new_url)

