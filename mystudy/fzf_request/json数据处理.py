#coding:utf-8
import requests
import json
pyload = {"yoyo":True,
          "json":False,
          "python":"22629643"
          }
print(type(pyload))
#转化成json格式
data_json = json.dumps(pyload)
print(type(data_json))
print(data_json)