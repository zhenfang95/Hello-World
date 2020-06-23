#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/6/15 20:32
# @author:AlexFu

'''线程同步'''
import threading
import time

threads = []
threadLock = threading.Lock()   #Lock方法可以实现线程同步

class myThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

#对于需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间
    def run(self):
        print("开始线程"+self.name)
        #获取锁，用于线程同步
        threadLock.acquire()
        print_time(threadName=self.name,delay=self.counter,counter=3)
        #释放锁，开启下一个线程
        threadLock.release()
        print("结束线程"+self.name)

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay)
        print("%s：%s" %(threadName,time.ctime(time.time())))
        counter -= 1

#创建新线程
thread01 = myThread(1,"nvnv",1)
thread02 = myThread(2,"gege",2)

#开启新线程
thread01.start()
thread02.start()

#添加线程到线程列表
threads.append(thread01)
threads.append(thread02)

#等待所有线程完成
for i in threads:
    i.join()
print("退出主线程")
