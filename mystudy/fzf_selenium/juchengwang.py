#coding:utf-8
from selenium import webdriver
import unittest
import time

"""
driver=webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
driver.implicitly_wait(5)   #隐性等待时间5秒
driver.maximize_window()
driver.get("http://passport.juooo.net.cn/User/login?return_url=http://www.juooo.net.cn/")
time.sleep(2)
driver.find_element_by_xpath("//li[@class='active']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='inputUserName']").clear()
driver.find_element_by_xpath("//input[@id='inputUserName']").send_keys("13097888019")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='inputPsw']").clear()
driver.find_element_by_xpath("//input[@id='inputPsw']").send_keys("123456")
time.sleep(2)
driver.find_element_by_xpath("//button[@id='login']").click()
time.sleep(2)
t = driver.find_element_by_id("js-get-username").text
#assert t == "13097888019","test fail"

print("我的账户名称：%s" % t)
if t == "13097888019":
    print("登录成功")
else:
    print("登录失败")
    
driver.quit()
"""
def login(driver,use,psw):
    driver.get("http://passport.juooo.net.cn/User/login?return_url=http://www.juooo.net.cn/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    time.sleep(2)
    driver.find_element_by_xpath("//li[@class='active']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='inputUserName']").clear()
    driver.find_element_by_xpath("//input[@id='inputUserName']").send_keys("13097888019")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@id='inputPsw']").clear()
    driver.find_element_by_xpath("//input[@id='inputPsw']").send_keys("123456")
    time.sleep(2)
    driver.find_element_by_xpath("//button[@id='login']").click()

def logout(driver):
    time.sleep(5)
    driver.find_element_by_xpath("//a[@href='http://passport.juooo.net.cn/User/logout' and @class='nav-link c9']").click()
    driver.refresh()  #刷新页面
    time.sleep(5)
    driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
    login(driver,"13097888019","123456")
    print("登录成功")
    logout(driver)


"""
class jcwtest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome("D:\\Chrome\\Application\\chromedriver.exe")
        self.driver.implicitly_wait(5)   #隐性等待时间5秒
        self.driver.maximize_window()
        self.driver.get("http://passport.juooo.net.cn/User/login?return_url=http://www.juooo.net.cn/")
        time.sleep(2)
    def test_mmdl(self):
        dr=self.driver
        dr.find_element_by_xpath("//li[@class='active']").click()
        time.sleep(2)
        dr.find_element_by_xpath("//input[@id='inputUserName']").clear()
        dr.find_element_by_xpath("//input[@id='inputUserName']").send_keys("13097888019")
        time.sleep(2)
        dr.find_element_by_xpath("//input[@id='inputPsw']").clear()
        dr.find_element_by_xpath("//input[@id='inputPsw']").send_keys("123456")
        time.sleep(2)
        dr.find_element_by_xpath("//button[@id='login']").click()
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
"""