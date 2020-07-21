#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/7/21 22:00

import pymysql

def Mysql(sql):
    try:
        conn = pymysql.connect(host='',
                            port='',
                            user='',
                            passwd='',
                            db='',
                            cursorclass=pymysql.cursors.DictCursor)   #以字典形式取数据
    except Exception as e:
        return e.args
    else:
        cur = conn.cursor()
        cur.execute(sql)
        data=cur.fetchall()
        return data
    finally:
        cur.close()
        conn.close()