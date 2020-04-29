#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/1/8 16:13

from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read())
        title = bsobj.body.h1    #取出body下的h1标签
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('bbububububub')
else:
    print(title)



