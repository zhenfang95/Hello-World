#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/5/8 16:27
# @author:AlexFu

import unittest
import requests
from unittest import mock

'''存在依赖关系的功能模拟测试'''
#支付类功能
class Payment():
    def requestOutofSystem(self,card_num,amount):
        '''
        请求第三方外部支付接口，并返回响应码
        :param card_num: 卡号
        :param amount: 支付金额
        :return: 返回状态码，200代表支付成功，500代表支付异常失败
        '''
        #第三方支付接口请求地址（故意写错）
        url = 'http://third.payment.pay/'
        #请求参数
        data = {'card_num':card_num,'amount':amount}
        response = requests.post(url=url,data=data)
        #返回状态码
        return requests.status_codes

    def doPay(self,user_id,card_num,amount):
        '''
        支付
        :param user_id:用户id
        :param card_num:卡号
        :param amount: 支付金额
        :return:
        '''
        try:
            #调用第三方支付接口请求进行真实扣款
            resp = self.requestOutofSystem(card_num,amount)
            print('调用第三方支付接口返回结果：%s'%resp)
        except TimeoutError:
            #如果超时就重新调用一次
            print('支付超时，重新支付')
            resp = self.requestOutofSystem(card_num,amount)

        if resp == 200:
            #返回第三方支付成功，则进行系统里面的扣款并记录支付记录等操作
            print('{0}支付{1}成功！！进行扣款并记录支付信息'.format(user_id,amount))
            return 'success'

        elif resp == 500:
            print('{0}支付{1}失败！！不进行扣款！！！'.format(user_id,amount))
            return 'fail'

#单元测试类
class payTest(unittest.TestCase):
    def test_pay_01_success(self):
        pay = Payment()
        #模拟第三方支付接口返回200
        pay.requestOutofSystem = mock.Mock(return_value=200)
        resp = pay.doPay(user_id=1,card_num='123456',amount=100)
        self.assertEqual('success',resp)

    def test_pay_02_fail(self):
        pay = Payment()
        #模拟第三方支付接口返回500
        pay.requestOutofSystem = mock.Mock(return_value=500)
        resp = pay.doPay(user_id=2,card_num='12345678',amount=200)
        self.assertEqual('fail',resp)

    def test_pay_03_time_success(self):
        pay = Payment()
        #模拟第三方接口首次支付超时，重次第二次成功
        pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError,200])
        resp = pay.doPay(user_id=3,card_num='123456789',amount=300)
        self.assertEqual('success',resp)

    def test_pay_04_time_fail(self):
        pay = Payment()
        #模拟第三方支付接口首次支付超时,重试第二次失败
        pay.requestOutofSystem = mock.Mock(side_effect=[TimeoutError,500])
        resp = pay.doPay(user_id=4,card_num='1234567890',amount=400)
        self.assertEqual('fail',resp)

if __name__ == '__main__':
    unittest.main()

