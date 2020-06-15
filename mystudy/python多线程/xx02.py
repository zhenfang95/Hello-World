#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/6/15 19:58
# @author:AlexFu

import threading
import time

exitFlag = 0

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s：%s" %(threadName,time.ctime(time.time())))
        counter -= 1

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程："+self.name)
        print_time(threadName=self.name,delay=self.counter,counter=5)
        print("退出线程："+self.name)

#创建新线程
thread01 = myThread(1,"haha",1)
thread02 = myThread(2,"kaka",2)

#开启新线程
thread01.start()  #start启动线程
thread02.start()
thread01.join()   #join等待至线程终止
thread02.join()
print("退出线程")