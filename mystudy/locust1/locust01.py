#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time:2019/10/14 15:45

from locust import HttpLocust,TaskSet,task

class MyTaskSet(TaskSet):
    @task(2)
    def test1(self):
        self.client.get('http://www.raincard.cn/api/v1/goods/list/admin/query')

    @task(1)
    def test2(self):
        self.client.get('http://www.raincard.cn/api/v1/order/list/admin/query')

class MyLocust(HttpLocust):
    task_set =  MyTaskSet
    min_wait = 3000
    max_wait = 5000