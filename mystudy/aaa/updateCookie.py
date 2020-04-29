#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/12/4 18:15

import requests
import unittest


class updateCookies(unittest.TestCase):
    def setUp(self):
        requests.packages.urllib3.disable_warnings()

    def test_lecturer_1(self):
        '''准线网环境_H5端VIP_cookie/讲师'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
            'cookie': 'XIAOEID=7c9d106445073f8087bedb200533d89c; channel=admin; cookie_channel=admin; cookie_session_id=C3hfQak7P4iMOJ2g5pOtz7KbM2rRtxLo; Hm_lvt_081e3681cee6a2749a63db50a17625e2=1575357565; Hm_lpvt_081e3681cee6a2749a63db50a17625e2=1575357565; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575357693; ko_token=0c58f7c889daa1a0ec41f0ea4d3c3414; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575364606; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ecb0c39831ce-08f4aa6626b7e-264a7546-273600-16ecb0c398436%22%2C%22%24device_id%22%3A%2216ecb0c39831ce-08f4aa6626b7e-264a7546-273600-16ecb0c398436%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""} X-Requested-With: com.tencent.mm '}
        url = ' https://apprnDA0ZDw4581.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoyLCJyZXNvdXJjZV90eXBlIjoyLCJyZXNvdXJjZV9pZCI6ImFfNWM0MTliZDI3NzdlMl9ONVNCYXVadiIsInByb2R1Y3RfaWQiOiIiLCJhcHBfaWQiOiJhcHBybkRBMFpEdzQ1ODEiLCJzaGFyZV91c2VyX2lkIjoidV81YmNlOTdhMWNlZWI1X3hRNlBORUxwMnQiLCJzaGFyZV90eXBlIjo1LCJleHRyYV9kYXRhIjoiMzAyIn0'
        r = requests.post(url=url, headers=headers,verify=False)
        self.assertEqual(r.json()['code'],0)
        self.assertEqual(r.json()['msg'],'操作成功')

    def test_student_1(self):
        '''准线网环境_H5端非VIP_cookie/学员'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
            'cookie': 'ko_token=fc134c4f2aa4ec9340767ff1ca0ddcb8; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22%24device_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""} X-Requested-With: com.tencent.mm'}
        url = ' https://apprnDA0ZDw4581.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoyLCJyZXNvdXJjZV90eXBlIjoyLCJyZXNvdXJjZV9pZCI6ImFfNWM0MTliZDI3NzdlMl9ONVNCYXVadiIsInByb2R1Y3RfaWQiOiIiLCJhcHBfaWQiOiJhcHBybkRBMFpEdzQ1ODEiLCJzaGFyZV91c2VyX2lkIjoidV81YmNlOTdhMWNlZWI1X3hRNlBORUxwMnQiLCJzaGFyZV90eXBlIjo1LCJleHRyYV9kYXRhIjoiMzAyIn0'
        r = requests.post(url=url, headers=headers,verify=False)
        self.assertEqual(r.json()['code'],0)
        self.assertEqual(r.json()['msg'],'操作成功')

    def test_student_2(self):
        '''内灰环境_H5端非VIP_cookie/学员'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
            'cookie': 'ko_token=d6be0623f90bb9704970919dc269f5b1; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22%24device_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""} X-Requested-With: com.tencent.mm'}
        url = ' https://app38itOR341547.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoiMiIsInJlc291cmNlX3R5cGUiOjIsInJlc291cmNlX2lkIjoiYV81Y2Q1Mzk0ODk2NTMxXzhBWXJneTU5IiwiYXBwX2lkIjoiYXBwMzhpdE9SMzQxNTQ3IiwicHJvZHVjdF9pZCI6IiJ9'
        r = requests.post(url=url, headers=headers,verify=False)
        self.assertEqual(r.json()['code'],0)
        self.assertEqual(r.json()['msg'],'操作成功')

    def test_lecturer_2(self):
        '''内灰环境_H5端VIP_cookie/讲师'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
            'cookie': 'Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575966610; sajssdk_2015_cross_new_user=1; ko_token=6037eed37850107ef2c00cf78174602a; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""}; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22u_5bd01c9754d5c_edPzAMVi6S%22%2C%22%24device_id%22%3A%2216eeeee12de10b-064b34c00afd54-264d7546-273600-16eeeee12dfd8%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216eeeee12de10b-064b34c00afd54-264d7546-273600-16eeeee12dfd8%22%7D; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575977498'}
        url = ' https://app38itOR341547.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoiMiIsInJlc291cmNlX3R5cGUiOjIsInJlc291cmNlX2lkIjoiYV81Y2Q1Mzk0ODk2NTMxXzhBWXJneTU5IiwiYXBwX2lkIjoiYXBwMzhpdE9SMzQxNTQ3IiwicHJvZHVjdF9pZCI6IiJ9'
        r = requests.post(url=url, headers=headers,verify=False)
        self.assertEqual(r.json()['code'],0)
        self.assertEqual(r.json()['msg'],'操作成功')

    def test_student_3(self):
        '''外灰环境_H5端非VIP_cookie/学员'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
            'cookie': 'ko_token=ee9e25bc24f721ff90c4a676b802dedb; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22%24device_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""} X-Requested-With: com.tencent.mm'}
        url = ' https://appXrWBVfHb8064.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoiMiIsInJlc291cmNlX3R5cGUiOjIsInJlc291cmNlX2lkIjoiYV81Y2I2YzgwMTQ4MWRkX2RCbDcyYU5HIiwiYXBwX2lkIjoiYXBwWHJXQlZmSGI4MDY0IiwicHJvZHVjdF9pZCI6IiJ9?cacheclean=1'
        r = requests.post(url=url, headers=headers,verify=False)
        self.assertEqual(r.json()['code'],0)
        self.assertEqual(r.json()['msg'],'操作成功')

    def test_lecturer_3(self):
        '''外灰环境_H5端VIP_cookie/讲师'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
            'cookie': 'ko_token=2a56370fa3bfdbe01db167723899c487; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575978318; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""}; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22u_5bd97dcfa39ee_nVIaVgeht9%22%2C%22%24device_id%22%3A%2216eefa0be7221-016cc4aa00d7b3-264d7546-273600-16eefa0be74118%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216eefa0be7221-016cc4aa00d7b3-264d7546-273600-16eefa0be74118%22%7D; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575978373'}
        url = ' https://appXrWBVfHb8064.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoiMiIsInJlc291cmNlX3R5cGUiOjIsInJlc291cmNlX2lkIjoiYV81Y2I2YzgwMTQ4MWRkX2RCbDcyYU5HIiwiYXBwX2lkIjoiYXBwWHJXQlZmSGI4MDY0IiwicHJvZHVjdF9pZCI6IiJ9?cacheclean=1'
        r = requests.post(url=url, headers=headers,verify=False)
        self.assertEqual(r.json()['code'],0)
        self.assertEqual(r.json()['msg'],'操作成功')

    def test_student_4(self):
        '''现网环境_H5端非VIP_cookie/学员'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
            'cookie': 'ko_token=6a52e87b8b3f0279790c4704ea9a72d4; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22%24device_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""} X-Requested-With: com.tencent.mm'}
        url = 'https://appAKLWLitn7978.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoyLCJyZXNvdXJjZV90eXBlIjoyLCJyZXNvdXJjZV9pZCI6ImFfNWM4OWY5NTM1NmViMl9RRWpENFl5UCIsInByb2R1Y3RfaWQiOiIiLCJhcHBfaWQiOiJhcHBBS0xXTGl0bjc5NzgifQ'
        r = requests.post(url=url, headers=headers,verify=False)
        self.assertEqual(r.json()['code'],0)
        self.assertEqual(r.json()['msg'],'操作成功')

    def test_lecturer_4(self):
        '''现网环境_H5端VIP_cookie/讲师'''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
            'cookie': 'ko_token=50425cd0fb8988bc1a7e901dde179b2b; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575978499; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""}; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22u_5be027b4693c4_M69a1lwsGM%22%2C%22%24device_id%22%3A%2216eefa38511ab-0098b8daf4ecbe-264d7546-273600-16eefa3851434%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216eefa38511ab-0098b8daf4ecbe-264d7546-273600-16eefa3851434%22%7D; XIAOEID=9f02ebb9b9d1e2a9f2b75f44e8af8264; cookie_referer=https%3A%2F%2Fwx4459d36c099a5f7b.h5.xiaoe-tech.com%2Fcontent_page%2FeyJ0eXBlIjoiMiIsInJlc291cmNlX3R5cGUiOjI5LCJyZXNvdXJjZV9pZCI6ImN6XzVkZTQ4MWEzNTdmY2NfYm1uOGJ0RE5tMiIsImFwcF9pZCI6ImFwcEFLTFdMaXRuNzk3OCIsInByb2R1Y3RfaWQiOiIifQ; channel=xiaoeh5; cookie_channel=xiaoeh5; cookie_session_id=wk0G3APT3ywk17omtR630begN4CWFBJh; Hm_lvt_32573db0e6d7780af79f38632658ed95=1575978506; Hm_lpvt_32573db0e6d7780af79f38632658ed95=1575978506; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575978513'}
        url = ' https://appAKLWLitn7978.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoyLCJyZXNvdXJjZV90eXBlIjoyLCJyZXNvdXJjZV9pZCI6ImFfNWM4OWY5NTM1NmViMl9RRWpENFl5UCIsInByb2R1Y3RfaWQiOiIiLCJhcHBfaWQiOiJhcHBBS0xXTGl0bjc5NzgifQ'
        r = requests.post(url=url, headers=headers,verify=False)
        self.assertEqual(r.json()['code'],0)
        self.assertEqual(r.json()['msg'],'操作成功')

    def test_Applet(self):
        '''准现网小程序cookie'''
        url = " https://app.xiaoe-tech.com/distribution_invite?app_id=apprnDA0ZDw4581"
        data = {
        "app_id":"apprnDA0ZDw4581",
        "app_type":"0",
        "app_version":"64",
        "buz_data":{"batch_id":"725509"},
        "user_id":"u_5bed1e1eaef52_o8RdJSNZCC",
        "encrypt_data":"0e53014b023dc80b8380df75fb313b7e",
        "buz_referer":"/page/invite_result/invite_result?bid=725509",
        "anon_user_id":"null",
        "anon_encrypt_data":"null",
        "submit_version":""}
        headers = {
            "content-type": "application/json",
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SCL-TL00 Build/HonorSCL-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 MicroMessenger/7.0.6.1460(0x27000636) Process/appbrand0 NetType/WIFI",
            "cookie":"ko_token=fc134c4f2aa4ec9340767ff1ca0ddcb8; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575963702; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575963702; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22u_5bed1e1eaef52_o8RdJSNZCC%22%2C%22%24device_id%22%3A%2216eeec1b6ab13a-054c73ae6b9e3-2b4d7d41-273600-16eeec1b6ac7c%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216eeec1b6ab13a-054c73ae6b9e3-2b4d7d41-273600-16eeec1b6ac7c%22%7D; dataUpJssdkCookie={'wxver':'7.0.9.1560','net':'WIFI','sid':""}"}
        r = requests.post(url=url,json=data,headers=headers,verify=False)
        self.assertEqual(r.json()['code'],7)
        self.assertEqual(r.json()['msg'],'\u60a8\u5df2\u8ba2\u8d2d\u8fc7\u8be5\u4ea7\u54c1!')


if __name__ == '__main__':
    unittest.main(verbosity=2)