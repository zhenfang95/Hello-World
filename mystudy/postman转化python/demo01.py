#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2020/5/9 10:46
# @Author: AlexFu

import json
import requests
import pytest

def readJson():
    return json.load(open('xiaoe.postman_collection.json','r',encoding='UTF-8'))['item']

@pytest.mark.parametrize('datas',readJson())  #参数化
def test_ai_Postman(datas):
    print()  #打印datas
    if datas['request']['method'] == 'POST':
        r = requests.request(method=datas['request']['method'],
                             url=datas['request']['url']['raw'],
                             json=json.loads(datas['request']['body']['raw']))
        assert r.json() == datas['expect']

if __name__ == '__main__':
    pytest.main(['-s','-v','demo01.py::test_ai_Postman'])
