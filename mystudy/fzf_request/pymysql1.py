#coding:utf-8
import pymysql
#数据配置
conn = pymysql.connect(host="10.0.2.153",
                       port=3306,
                       user="root",
                       db="gw_20190429",
                       charset="utf-8")
cr=conn.cursor(pymysql.cursors.DictCursor)
cr.execute('(SELECT * FROM juo_coupon)')
result = cr.fetchall()
print(result)
