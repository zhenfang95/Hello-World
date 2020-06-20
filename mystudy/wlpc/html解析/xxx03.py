#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/1/13 15:59

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''正则表达式和BeautifulSoup'''
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html.read())
#正则表达式和BeautifulSoup通过商品图片的文件路径查找图片地址
images = bsobj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")}) #取出图片的相对路径
for image in images:
    print(image["src"])

'''Lambda表达式'''
lam = bsobj.findAll(lambda tag:tag.attrs)

