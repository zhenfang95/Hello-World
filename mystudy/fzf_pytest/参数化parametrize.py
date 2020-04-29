#!/usr/bin/env python

import pytest
#实现检查一定的输入和期望输出测试功能的典型例子
@pytest.mark.parametrize('test_input,expected',
                         [('3+5',8),
                          ('2+4',6),
                          ('6*9',44),
                          #pytest.param('6*9',44,marks=pytest.mark.xfail), #标记单个测试实例在参数化
                          ])
#从上面取出数据执行用例
def test_eval(test_input,expected):
    print('-----开始用例-----')
    assert eval(test_input) == expected


# 参数组合
# @pytest.mark.parametrize('x', [0, 1])
# @pytest.mark.parametrize('y', [2, 3])
# def test_foo(x, y):
#     print("测试数据组合：x->%s,y->%s" % (x, y))


if __name__ == '__main__':
    pytest.main()


