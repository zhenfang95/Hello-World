#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @time:2020/10/9 16:31

import psutil
import time
import datetime
from threading import Timer

def MonitorSystem():
    #获取cpu使用情况
    cpuper = psutil.cpu_percent()
    #获取内存使用情况：系统内存大小，使用内存，有效内存，内存使用率
    mem = psutil.virtual_memory()
    #内存使用率
    memper = mem.percent
    #获取当前时间
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} cpu:{cpuper}%, mem:{memper}%'
    print(line)

    # 启动定时器任务，每三秒执行一次
    Timer(3, MonitorSystem).start()

def MonitorNetWork():
    #获取网络收信息
    netinfo = psutil.net_io_counters()
    #获取当前时间
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    line = f'{ts} bytessent={netinfo.bytes_sent}, bytesrecv={netinfo.bytes_recv}'
    print(line)

    # 启动定时器任务，每一秒执行一次
    Timer(1, MonitorNetWork).start()

MonitorSystem()
MonitorNetWork()
