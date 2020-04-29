#!/usr/bin/env python
import requests
import json
import unittest
import re
import HTMLTestRunner

class Test(unittest.TestCase):
    def login(self):
        '''登录'''
        pydata={'username':'15217043402','password':'fzf123456','loginType':3}
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        url='http://passport.com.juooo.net.cn/User/doLoginRoute'
        s=requests.session()
        r=s.post(url,headers=headers,data=pydata)
        #获取登录响应头中的cookie，并以json格式输出
        cookie=r.cookies
        cook=requests.utils.dict_from_cookiejar(cookie)
        return cook

    def test_buyTickets(self):
        '''进入结算页'''
        cookies=self.login()
        pydata={'type':1,'tickets':'442922_1_2'}
        url='http://item.com.juooo.net.cn/Index/buyTickets'
        r=requests.post(url,data=pydata,cookies=cookies)
        c=r.content.decode('utf-8')
        j=json.loads(c)       #反序列化输出
        self.assertEqual(j['code'],'ok')
        k=re.findall(r'_k=(.+)&',c)       #正则表达式提取k值
        return k

    def test_createOrder(self):
        '''提交订单'''
        cookies=self.login()
        pydata={'_k':self.test_buyTickets(),'type':1,'isClass':'buyTicket','payId':666,
                'userCertificationId':0,'shippingId':4,'userName':'南山','mobile':'15217043401',
                'activityType':2,'isCard':0,'isScore':0,'isUserMoney':0,'frontOrderAmount':1080.00,
                'culture':0,'topay_conf':1,'deductionWay':3}
        r=requests.post('http://buy.com.juooo.net.cn/Index/createOrder',data=pydata,cookies=cookies)
        c=r.content.decode('utf-8')
        j=json.loads(c)
        self.assertEqual(j['code'],'200')
        return j

    def run_case(self,all_case):
        '''运行测试用例'''
        feil='report.html'
        fb=open(feil,'wb')
        runner=HTMLTestRunner.HTMLTestRunner(stream=fb,title='接口自动化测试报告',description='下单购买商品')
        runner.run(all_case)
        fb.close()

if __name__ == '__main__':
    suite=unittest.TestSuite()   #构造测试集
    suite.addTest(Test('test_buyTickets'))
    suite.addTest(Test('test_createOrder'))
    per=Test()
    per.run_case(suite)



