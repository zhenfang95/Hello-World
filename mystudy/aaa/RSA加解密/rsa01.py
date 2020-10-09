#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2020/8/5 11:21

import rsa
import base64
import json
from urllib.parse import urlencode

'''通常使用中, 会先对数据进行bas64加密, 再对加密后的内容使用rsa加密, 最后对rsa解密后的内容进行bas64解密.'''

# 密文写入文件
def CypherWriter(CypherCodename):
    f = open('Cyphertext.txt', 'wb')
    f.write(CypherCodename)
    f.close()

#生成一对公钥和私钥并保存
pubkey,privkey = rsa.newkeys(2048)

pub = pubkey.save_pkcs1()
pri = privkey.save_pkcs1()
with open('pubkey.pem','wb') as f,open('privkey.pem','wb') as f1:
    f.write(pub)
    f1.write(pri)

#从文件中读出公钥和私钥
with open('pubkey.pem','rb') as f,open('privkey.pem','rb') as f1:
    pub=f.read()
    pri=f1.read()
    #转为原始状态
    pubkey = rsa.PublicKey.load_pkcs1(pub)
    privkey = rsa.PrivateKey.load_pkcs1(pri)

msg = {
    "version": "2.0",
    "charset": "UTF-8",
    "messageId": "02dxxadwf3f3a29674e674e6",
    "guestId": "10100",
    "appId": "10103",
    "signType": "RSA2",
    "reqTime": "2020043011212",
    "beginTime": "20200804-121212",
    "endTime": "20200805-231212",
    "deviceId": "04181100646",
    "pspId": "2",
    "businessDate": "20200805"
}
#对字典进行从小到大排序
ww = dict(sorted(msg.items(),key=lambda x:x[0],reverse=False))
#将字段转换为url编码格式
aa = urlencode(ww).encode()
print(aa)

#用公钥加密，并用Base64编码后输出
info = rsa.encrypt(json.dumps(msg).encode(),pubkey)
info64 = base64.b64encode(info)
CypherWriter(info64)
print(info64)

# 通过Base64解码，用私钥解密
msg1 = base64.b64decode(info64)
mssg = rsa.decrypt(msg1,privkey)
print(mssg.decode('utf-8')) #解码






