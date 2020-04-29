#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/4/10 14:30

import mysql.connector

mydb = mysql.connector.connect(
    host = '192.168.231.128',
    user = 'root',
    passwd = '123456',
    database = 'alexdata' #连接到数据库alexdata
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM cousr')

myresult = mycursor.fetchall() #返回全部结果
#myresult = mycursor.fetchone() #返回结果的第一行

for i in myresult:
    print(i)