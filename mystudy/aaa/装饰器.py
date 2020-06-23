#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/6/16 17:11
# @author:AlexFu

import time

#写一个简单的装饰器
def debug(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        time.sleep(1)
        print("[DEBUG]：error {}".format(func.__name__))
        end_time = time.time()
        time_se = end_time - start_time
        print("运行时长：{}".format(time_se))
        return func(*args,**kwargs)
    return wrapper    #使用动态参数，返回的方法不需要待括号

@debug
def say_hello(ww):
    print("hello {}!".format(ww))



#生成log装饰器
def loging(level):
    def wrapper(func):
        def inner_wrapper(*args,**kwargs):
            print("[{}]: enter function {}()".format(level,func.__name__))
            return func(*args,**kwargs)
        return inner_wrapper
    return wrapper

@loging(level="INFO")
def say(somthing):
    print("say {}！".format(somthing))

@loging(level="DEBUG")
def do(somthing):
    print("do {}！".format(somthing))

if __name__ == "__main__":
    say("hello world")
    do("my good")
