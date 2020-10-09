#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/11 17:13

import json,base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from urllib.parse import urlencode

#商户对应私钥
private_key = ''

def front_wallet_rsa(private_key,sign_data):
    sign_data.pop('sign')  #删除字段sign
    data_sort = dict(sorted(sign_data.items(),key=lambda x:x[0],reverse=False))  #对字典进行从小到大排序
    sign_data_url = urlencode(data_sort).encode('utf-8')   #将字段转换为url编码格式
    private_keyBytes = base64.b64decode(private_key)
    priKey = RSA.importKey(private_keyBytes)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = SHA256.new()
    hash_obj.update(sign_data_url)
    signature = base64.b64encode(signer.sign(hash_obj))
    sign = signature.decode("utf-8")
    sign_data['sign'] = sign
    return json.dumps(sign_data)