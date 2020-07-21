#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/4/10 15:40

import pymysql

mydb = pymysql.connector.connect(
    host = '192.168.231.128',
    user = 'root',
    passwd = '123456',
    database = 'alexdata' #连接到数据库alexdata
)

mycursor = mydb.cursor()

sql = "UPDATE cousr SET content = %s WHERE name = %s"
val = ('你好，深圳！','alex002')
mycursor.execute(sql,val)

mydb.commit()  #确认需要更改，否则表不会有任何改变

print(mycursor.rowcount)
