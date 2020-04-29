#coding:utf-8
import requests

url = "https://www.zto.com/express/expressCheck.html?txtBill=75147810223179"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
s = requests.session()
r = s.get(url,headers=headers,verify=False)
result = r.json()
data = result["data"]  #获取data里面的内容
print(data)
print(data[0])
get_result = data[0]["context"] #获取已签收标签
print(get_result)

if "已签收" in get_result:
    print("快递单已签收成功")
else:
    print("未签收")


