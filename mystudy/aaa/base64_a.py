#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/25 10:11

import base64
import json

a = {"src_url":"https://wxdd198a901fa24220.h5.xiaoe-tech.com/v1/course/text/i_5db11cfe841f9_nF0uzvbx?type=2","jump_data":{"back_url":"https://wxdd198a901fa24220.h5.xiaoe-tech.com/v1/course/text/i_5db11cfe841f9_nF0uzvbx?type=2"},"out_order_id":"","app_id":"apprnDA0ZDw4581","order_id":""}
#json.dumps()把dict转为str，encode()把str类型转为bytes类型
aa = json.dumps(a).encode()
#base64加密
s = base64.b64encode(aa)   #base64只能对bytest类型进行加密
ss = str(s,'utf8') #把加密后的参数变为字符串并去掉‘b’
#base64解密
zz = base64.b64decode(ss)
print(zz)
