#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/4/16 17:51

import requests
import re

headers = {'Cookie':'b_user_token_inside=token_5e95b08a66b73RoNRWyPSpxeLNo8L59tr'}

def shoplist():
    url = 'http://admin.inside.xiaoe-tech.com/shop_list'
    result = requests.get(url=url,params=None,headers=headers)
    lt=re.findall(r'shop_id":"(.+?)",',result.text)[0]
    assert'ok',result.json()['msg']
    return lt

def choose_shop():
    url = 'http://admin.inside.xiaoe-tech.com/choose_shop'
    result = requests.get(url=url,params='app_id='+shoplist(),headers=headers)
    assert '登录成功',result.json()['msg']
    return result.json()

print(choose_shop())
