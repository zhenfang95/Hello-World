#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/4/10 11:20

import mysql.connector

mydb = mysql.connector.connect(
    host = '192.168.231.128',
    user = 'root',
    passwd = '123456',
    database = 'alexdata' #连接到数据库alexdata
)

#创建数据库
mycursor = mydb.cursor()
#mycursor.execute('CREATE DATABASE alexdata')

#检查数据库是否存在
mycursor.execute('SHOW DATABASES')
for i in mycursor:
    print(i)

#检查表
mycursor.execute('SHOW TABLES')
for i in mycursor:
    print(i)
