#coding:utf-8
class xxx():
    def addd(self,name):
        print("引用成功",name)

aList = [123,"xyz","zara","abc", 123]
print(aList.count(2))

import requests

header={'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
        'cookie':'ko_token=9cabb38a25251dd5bf744ce030762ca8; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575364679; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22%24device_id%22%3A%2216ecb0d592465-04417d9f426eb4-2b4a7d41-273600-16ecb0d592524a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""} X-Requested-With: com.tencent.mm'}
url=' https://apprnDA0ZDw4581.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoyLCJyZXNvdXJjZV90eXBlIjoyLCJyZXNvdXJjZV9pZCI6ImFfNWM0MTliZDI3NzdlMl9ONVNCYXVadiIsInByb2R1Y3RfaWQiOiIiLCJhcHBfaWQiOiJhcHBybkRBMFpEdzQ1ODEiLCJzaGFyZV91c2VyX2lkIjoidV81YmNlOTdhMWNlZWI1X3hRNlBORUxwMnQiLCJzaGFyZV90eXBlIjo1LCJleHRyYV9kYXRhIjoiMzAyIn0'
r = requests.post(url=url,headers=header)
print(r.json())

header1={'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.126 MQQBrowser/6.2 TBS/044432 Mobile Safari/537.36 MMWEBID/4134 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/tools',
        'cookie':'XIAOEID=7c9d106445073f8087bedb200533d89c; channel=admin; cookie_channel=admin; cookie_session_id=C3hfQak7P4iMOJ2g5pOtz7KbM2rRtxLo; Hm_lvt_081e3681cee6a2749a63db50a17625e2=1575357565; Hm_lpvt_081e3681cee6a2749a63db50a17625e2=1575357565; Hm_lvt_17bc0e24e08f56c0c13a512a76c458fb=1575357693; ko_token=dc1cb9a6bf4cb301aaa5484a2120b8a4; Hm_lpvt_17bc0e24e08f56c0c13a512a76c458fb=1575364606; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ecb0c39831ce-08f4aa6626b7e-264a7546-273600-16ecb0c398436%22%2C%22%24device_id%22%3A%2216ecb0c39831ce-08f4aa6626b7e-264a7546-273600-16ecb0c398436%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; dataUpJssdkCookie={"wxver":"7.0.9.1560","net":"WIFI","sid":""} X-Requested-With: com.tencent.mm '}
url1=' https://apprnDA0ZDw4581.h5.xiaoeknow.com/audio_index_lazy/eyJ0eXBlIjoyLCJyZXNvdXJjZV90eXBlIjoyLCJyZXNvdXJjZV9pZCI6ImFfNWM0MTliZDI3NzdlMl9ONVNCYXVadiIsInByb2R1Y3RfaWQiOiIiLCJhcHBfaWQiOiJhcHBybkRBMFpEdzQ1ODEiLCJzaGFyZV91c2VyX2lkIjoidV81YmNlOTdhMWNlZWI1X3hRNlBORUxwMnQiLCJzaGFyZV90eXBlIjo1LCJleHRyYV9kYXRhIjoiMzAyIn0'
r1 = requests.post(url=url1,headers=header)
print(r.json())

