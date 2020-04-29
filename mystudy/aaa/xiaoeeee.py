#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/1/2 20:19

import requests

header={'Content-Type':'application/json',
        'cookie':'ko_token=12312312qw'}

i=0
while i<5:
    r = requests.get(url='http://119.29.200.227:1215/',headers=header)
    print(r.text)
    i+=1

