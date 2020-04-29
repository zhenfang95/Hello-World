import requests

header={
        "key": "Content-Type",
        "name": "Content-Type",
        "value": "application/json",
        "type": "text"
        }
#url='http://119.29.200.227:7777/gray/selectors'
url='http://119.29.200.227:7777/rate_limiting/selectors/{{rate_limiting_selector}}/rules'
url2='http://119.29.200.227:7777/rate_limiting/config'

#body={"selector":{"name":"h5_wechat","enable":True}}
body={
    "rule":{
        "name":"ip 1分钟100次",
        "extractor":{
            "type":1,
            "extractions":[
                {
                    "type":"IP"
                }
            ]
        },
        "handle":{
            "period":60,
            "count":100
        },
        "enable":True
    }
}

#rr=requests.post(url,data=body,headers=header)
r=requests.get(url2,headers=header)
print(r.json())
