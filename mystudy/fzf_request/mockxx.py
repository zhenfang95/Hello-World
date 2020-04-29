#!/usr/bin/env python
#coding:utf-8
import mock
#print('查看mock库常用方法：',dir(mock))
#print('查看mock库详细的帮助信息：',help(mock))

# 删除文件
'''import os
class Remove():
    def rmdir(self,path=r'D:\www'):
        r = os.rmdir(path)
        if r == None:
            return "删除成功"
        else:
            return "删除失败"
    def exists_get_rmdir(self):
        return self.rmdir()

rr = Remove()
rr.rmdir()
rr.exists_get_rmdir()'''

mock=mock.Mock()
mock.info.return_value="hello mock"
w = mock.info
print(w)
class F():
    def info(self):
        return "hello mock"
f = F()
print(f.info())
