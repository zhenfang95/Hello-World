#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/5/11 14:21
# @author:AlexFu

import pytest

#输入三种测试数据，断言同时满足三种情况
@pytest.mark.parametrize(('x','y'),[(1,1),(1,0),(0,1)])
def test_simpie_assume(x,y):
    print('测试数据x=%s，y=%s'%(x,y))
    #同时满足下面三个断言才pass
    pytest.assume(x==y)
    pytest.assume(x+y>1)
    pytest.assume(x>1)

if __name__ == '__main__':
    pytest.main(['-s','-v','py断言失败后继续执行.py'])
