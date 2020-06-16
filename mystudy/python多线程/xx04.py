#!/usr/bin/env python 
#-*- coding:utf-8 -*-
# @time  :2020/6/16 10:30
# @author:AlexFu

import queue
import threading
import time

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("开启线程"+self.name)
        process_data(threadName=self.name,q=self.q)
        print("退出线程"+self.name)

#为线程定义一个函数
def process_data(threadName,q):
    while not exitFlag == 1:
        queueLock.acquire()
        if not workQueue.empty():  #empty()判断如果队列为空，返回true，反正返回false
            data = q.get()
            queueLock.release()
            print("%s processing %s" %(threadName,data))

        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1","Thread-2","Thread-3"]
nameList = ["one","two","three","four","five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

#创建新线程
for tName in threadList:
    thread = myThread(threadID,tName,workQueue)
    thread.start() #启动线程
    threads.append(thread)
    threadID += 1

#填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)   #put()写入队列
queueLock.release()

#等待队列清空
while not workQueue.empty():
    pass

#通知线程是时候退出了
exitFlag = 1

#等待所有线程我完成
for t in threads:
    t.join()
print("退出主线程")