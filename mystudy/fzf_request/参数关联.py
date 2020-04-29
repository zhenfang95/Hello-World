#coding:utf-8
import requests
from requests.cookies import RequestsCookieJar
# 先打开登录首页，获取部分cookie
url ="https://account.cnblogs.com/Account/SignIn"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
s = requests.session()
# verify=False是避免ssl认证，https是ssl加密请求
r = s.get(url,headers=headers,verify=False)
print(r.cookies)
c = requests.cookies.RequestsCookieJar()   #获取cookie
c.set('.AspNetCore.Antiforgery.b8-pDmTq1XM','CfDJ8JcopKY7yQlPr3eegllP76MTfpZyQ-g3Q85Vfjn83fSr_AF4UxUyoS8X56-3YM_fm-2QrBFd0-l-gmAdxcG3hNfFr7oq3nZEd2M6V89pq1IrAajyQYI8X-gsGBRoBv36oauDAvZWG7KNwEYouBhnHB4')
c.set('.AspNetCore.Session','CfDJ8JcopKY7yQlPr3eegllP76MNPXi1PvBUZA9yoUx5MKeJGoDKMJ%2BawtfIt4AI03QnFif3FevqIpZNqecllcz%2FRu7ecawU6BUDk3nKGQni8AEnXaokdxmamOnQve9iZPSmcmpLvlUZPbJW74N2dC%2B54V2SzLdsCAYXlOg4GU1u9YqU')
s.cookies.update(c)
print(s.cookies)
# 登录成功后保存编辑内容
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1",headers=headers,verify=False)
# 保存草稿箱
url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body ={"__VIEWSTATE":"",
        "__VIEWSTATEGENERATOR":"FE27D343",
        "Editor$Edit$txbTitle":"测试测试",
        "Editor$Edit$EditorBody":"喔喔哟哟",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$Advanced$txbEntryName":"",
        "Editor$Edit$Advanced$txbExcerpt":"",
        "Editor$Edit$Advanced$txbTag":"",
        "Editor$Edit$Advanced$tbEnryPassword":"",
        "Editor$Edit$lkbDraft":"存为草稿",
}
r2 = s.post(url2,data=body,verify=False)
#获取当前url
print(r2.url)

#正则表达式提取需要的参数值
import re
postid = re.findall(r'postid=(.+?)&',r2.url)
print(postid)  #这里是list
#提取为字符串
print(postid[0])

#删除草稿箱
url3 = "https://i.cnblogs.com/post/delete "
json3 = {"postId":postid[0]}
r3 = s.post(url3,json=json3,verify=False)
print(r3.json())