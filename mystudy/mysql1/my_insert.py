#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/4/10 14:11

import mysql.connector
import time

mydb = mysql.connector.connect(
    host = '192.168.231.128',
    user = 'root',
    passwd = '123456',
    database = 'alexdata' #连接到数据库alexdata
)

mycursor = mydb.cursor()

sql = "INSERT INTO cousr (name,content,create_at,update_at,t_type) VALUES (%s,%s,%s,%s,%s)"

#插入单行
val = ("alex001","没有不可能",time.localtime(time.time()),time.localtime(time.time()),0)
#mycursor.execute(sql,val)

#插入多行
val1 = [("alex002","只有不愿意",time.localtime(time.time()),time.localtime(time.time()),1),
        ("alex003","你好",time.localtime(time.time()),time.localtime(time.time()),1),
        ("alex004","你不好",time.localtime(time.time()),time.localtime(time.time()),1),
        ("alex005","我很好",time.localtime(time.time()),time.localtime(time.time()),0),
        ("alex006","深圳你不好",time.localtime(time.time()),time.localtime(time.time()),1),
        ("alex007","我以为不好",time.localtime(time.time()),time.localtime(time.time()),0)
        ]
mycursor.executemany(sql,val1)

mydb.commit()  #确认需要更改，否则表不会有任何改变

print(mycursor.rowcount) #返回最后一行的id