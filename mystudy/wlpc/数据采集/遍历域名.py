#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/1/13 16:39

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsobj = BeautifulSoup(html)
for link in bsobj.findAll("a"):
    if 'href' in link.attrs:   #用attrs是从得到的链接里面找到相对应的属性
        print(link.attrs['href'])