#!/usr/bin/env python 
import pytest

'''既然有setup那就有teardown,fixture里面的teardown用yield来唤醒teardown的执行'''
#scope="module"---->整个用例开始前只执行一次
@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")

    yield
    print("执行teardown：关闭浏览器")

def test_01(open):
    print("用例1：搜索python-1")
    # 如果第一个用例异常了，不影响其他的用例执行
    raise NameError   #模拟异常

def test_02(open):
    print("用例2：搜索python-2")

def test_03(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main()