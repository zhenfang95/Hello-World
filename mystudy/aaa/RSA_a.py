#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/11 13:46

import json,base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from urllib.parse import urlencode

#商户对应私钥
private_key = 'MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAL6qwXEI5tKPjXOQ\nNUl/cchAWvnXITYOP3ley3PBsXKHdFIA6e6b7NgLWE5zvM9BqE0FC4I7I7oeGxz6\nvPpN8sqpKp22mgarTabY1/nh9tlIKU6BaLaOJXWdQbN30oVSjiz/b/VQmZDg3utO\nEPU8VMyeBmMjzJQ4yOiXfg0hHsOxAgMBAAECgYA2dlALGZ/VRWwCNo8CD4VQzhEu\njGTQLAG1iX5T8l/ddxOi2N/5aFCe5Z6zyhuEmBya43YGHR53a2ITRQv1844GFiuI\n24xiFgtKVlYIEI8cANJah7ubXJ5g+kHuXGO9pRJ2nLoNggOUPyvUUFmlbB2ZQ4x4\nHvIOX9Ftc+yKdGzwgQJBAP0C8vX6VLVGDMM0rMj/eVtaZMCikByl7iv1c+ifEfMQ\nuX2bcAEm8LL2jd6DZcgLr+zg1RiWIbrlMkRXQ5AEZw8CQQDA60phz205PPwWEgmd\nro9oBF1csmpg9GcpDY158sQ1snXs0OFC9gp67OmFrhVIe80IJu1JNrPjasBRC62L\n+Ck/AkA656bdMczq70YlZGwd16zPYfo3ByH6KX+L6Hd13yL0rh4hakDnY8OCRvi8\np2bY7i+lPKsgMEPmGVpcotxt+ThtAkAULQdcb1sW71/V1xEWYpkw4bP569bgSO85\nBefT5yXKD93xZG8Kl7zE2l4Z0vj62ae5wIh0bbomgJWYZEZEKzH1AkEAlAYEEwoO\nKqGerHHacPLB0Y1oEKM7OLzDYHzJXxzYRr1jds9jr4UdquakMDubeofTpbfbcO4B\nimvtZgCBxEoQ2A=='
print(type(private_key))
data ={
    "charset": "UTF-8",
    "appId": "10103",
    "messageId": "02dxxadwf3f3a29674e674e6",
    "signType": "RSA2",
    "sign":"wewqewqe2131212312123",
    "reqTime": "1590403148703",
    "guestId": "10100",
    "version": "2.0",
    "traceNum": 1,
    "numPassId": 9999
}

def front_wallet_rsa(private_key,sign_data):
    sign_data.pop('sign')  #删除字段sign
    data_sort = dict(sorted(sign_data.items(),key=lambda x:x[0],reverse=False))  #对字典进行从小到大排序
    sign_data_url = urlencode(data_sort).encode('utf-8')   #将字段转换为url编码格式
    private_keyBytes = base64.b64decode(private_key)
    print(private_keyBytes)
    priKey = RSA.importKey(private_keyBytes)
    signer = PKCS1_v1_5.new(priKey)
    hash_obj = SHA256.new()
    hash_obj.update(sign_data_url)
    signature = base64.b64encode(signer.sign(hash_obj))
    sign = signature.decode("utf-8")
    sign_data['sign'] = sign
    return json.dumps(sign_data)

result = front_wallet_rsa(private_key=private_key,sign_data=data)
print(result)
