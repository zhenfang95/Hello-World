#coding:utf-8
import requests
import unittest
import HTMLTestRunner
from fzf_request.logger1 import Log
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.url = "http://passport.juooot.com/User/doLoginRoute"
    @classmethod
    def tearDownClass(self):
        pass
    def test_case01(self):
        '''正确用户名登陆'''
        paydata = {"username":"13097888019","password":"123456","loginType":"3"}
        r = requests.post(self.url,data=paydata)
        j = r.json()
        self.assertEqual(j["msg"],"登录成功")
        return r
    def test_case02(self):
        '''用户名含空格'''
        paydata = {"username": " 13097888019 ", "password": "123456", "loginType": "3"}
        r = requests.post(self.url,data=paydata)
        j = r.json()
        self.assertEqual(j["msg"],"用户不存在或被禁用")
        return r
    def test_case03(self):
        '''错误用户名登陆'''
        paydata = {"username": "130978880191", "password": "123456", "loginType": "3"}
        r = requests.post(self.url, data=paydata)
        j = r.json()
        self.assertEqual(j["msg"],"用户不存在或被禁用")
        return r

    def test_case03_1(self):  #中间插入测试用例
        pass

    def test_case04(self):
        '''输入特殊字符组合'''
        paydata = {"username": "130##@*&^nmj", "password": "123456", "loginType": "3"}
        r = requests.post(self.url,data=paydata)
        j = r.json()
        self.assertEqual(j["msg"],"用户不存在或被禁用")
        return r

if __name__=="__main__":
    #unittest.main()
    #suite = unittest.TestSuite()  #构造测试集
    # suite.addTest(Login("test_case01"))
    # suite.addTest(Login("test_case02"))
    # suite.addTest(Login("test_case03"))
    # suite.addTest(Login("test_case04"))
    # feil = "E:\\tsetdate\\HTMLTest\\report.html"
    # fp = open(feil,"wb")
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="自动化测试报告",description="juoo登录模块")
    # runner.run(suite)
    # log = Log()

    suite = unittest.TestSuite(unittest.makeSuite(Login))     # 加载整个类的测试用例
    unittest.TextTestRunner(verbosity=2).run(suite)

