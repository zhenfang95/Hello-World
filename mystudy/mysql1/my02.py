#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/4/10 11:31

import mysql.connector

mydb = mysql.connector.connect(
    host = '192.168.231.128',
    user = 'root',
    passwd = '123456',
    database = 'alexdata' #连接到数据库alexdata
)

mycursor = mydb.cursor()

#新建表
#mycursor.execute('CREATE TABLE cousr ( id INT(50) NOT NULL AUTO_INCREMENT, name VARCHAR(255), content VARCHAR(255), create_at VARCHAR(255),update_at VARCHAR(255), PRIMARY KEY (id) )')

#添加字段
#mycursor.execute('ALTER TABLE cousr ADD COLUMN t_type INT(12)')

#删除表
mycursor.execute('DROP TABLE cess')

