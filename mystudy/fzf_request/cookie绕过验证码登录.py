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
        "Editor$Edit$txbTitle":"这是3111",
        "Editor$Edit$EditorBody":"<p>这里111：http://www.cnblogs.com/yoyoketang/</p>",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$Advanced$txbEntryName":"",
        "Editor$Edit$Advanced$txbExcerpt":"",
        "Editor$Edit$Advanced$tbEnryPassword":"",
        "Editor$Edit$lkbDraft":"存为草稿",
}
r2 = s.post(url2,data=body,verify=False)
print(r.content)
