#!/usr/bin/env python
#-*- coding:utf-8 -*-
# @time:2020/1/10 17:01

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsobj = BeautifulSoup(html.read())
namelist = bsobj.findAll("span",{"class":"green"})   #利用findALL函数抽取只包含在<span class="green"></span> 标签里的文字
title = bsobj.findAll({"h1","h2","h3","4","h5","h6"})  #取出html中所有标题标签
ys = bsobj.findAll("span",{"class":{"green","rad"}})  #取出html中红色与绿色2种颜色的span标签
# for name in namelist:
#     print(name.get_text())     #.get_text() 会把你正在处理的 HTML 文档中所有的标签都清除，然后返回一个只包含文字的字符串

#查找网页中包含“the prince”内容的标签数量
namel = bsobj.findAll(text="the prince")
#获取指定属性的标签,以下2行代码输出结果一样
alltext = bsobj.findAll(id="text")
alltext1 = bsobj.findAll("",{"id":"text"})

