#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/29 20:41

import requests

url = "https://sh.file.myqcloud.com/files/v2/1252524126/wechatapppro/appbOVM8zDL7885/image/cmVzb3VyY2UtY291cnNlQXJ0aWNsZS05Njg2NzU1NA.jpg?sign=DGgRf8upuNAyZ5umfIZWBaP1vlhhPTEyNTI1MjQxMjYmaz1BS0lER1VqY0tzZ0ZFN2xHYm5oNExZZ3BMang0emttb3Q3emcmZT0xNTcyMzUzNTkyJnQ9MTU3MjM1Mjk5MiZyPTMwMTExNTI1OSZmPSZiPXdlY2hhdGFwcHBybw%3D%3D"
files = {'img':('414312cmVzb3VyY2UtY291cnNlQXJ0aWNsZS02MTc1NDY0Ng.jpg',open('D:\\414312cmVzb3VyY2UtY291cnNlQXJ0aWNsZS02MTc1NDY0Ng.jpg','rb'),'image/png',{})}
res = requests.post(url=url,data={'op':'upload','insertOnly':0},files=files)
print(res.text)


