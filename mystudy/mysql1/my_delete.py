#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/4/10 15:33

import mysql.connector

mydb = mysql.connector.connect(
    host = '192.168.231.128',
    user = 'root',
    passwd = '123456',
    database = 'alexdata' #连接到数据库alexdata
)

mycursor = mydb.cursor()

sql = "DELETE FROM cousr WHERE name = %s"
val = ('alex004',)
mycursor.execute(sql,val)

mydb.commit()  #确认需要更改，否则表不会有任何改变

print(mycursor.rowcount)