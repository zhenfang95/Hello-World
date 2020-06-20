#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/6/20 19:52

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

'''正则表达式和BeautifulSoup'''
html = urlopen("https://tieba.baidu.com/f?kw=%E6%B7%B1%E5%9C%B3%E5%BE%AE%E4%BF%A1%E7%BE%A4&traceid=")
bsobj = BeautifulSoup(html.read())
#正则表达式和BeautifulSoup通过商品图片的文件路径查找图片地址
images = bsobj.findAll("img",{"src":re.compile("http:\/\/tiebapic.baidu.com\/forum\/wh%3D200%2C90%3B\/sign=b07f5d26dd8065387bbfac11a7ed8d7d\/22675e504fc2d562a6590885f01190ef77c66ce1\.jpg")}) #取出图片的路径
for image in images:
    print(image["src"])
