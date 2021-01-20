#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @time:2020/10/9 16:39

import datetime
import schedule
import time

def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func  time :',ts)
def func2():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：',ts)
def tasklist():
    #清空任务
    schedule.clear()
    #创建一个按秒间隔执行任务
    schedule.every(1).seconds.do(func)
    #创建一个按2秒间隔执行任务
    schedule.every(2).seconds.do(func2)
    schedule.every().day.at("10:30").do(func2)
    #执行10S
    # for i in range(10):
    #     schedule.run_pending()
    #     time.sleep(1)

    while True:
        schedule.run_pending()
tasklist()

#schedule.every(1)创建Job, seconds.do(func)按秒间隔查询并执行
schedule.every(1).seconds.do(func)
#添加任务按分执行
schedule.every(1).minutes.do(func)
#添加任务按天执行
schedule.every(1).days.do(func)
#添加任务按周执行
schedule.every().weeks.do(func)
#添加任务每周1执行，执行时间为下周一这一时刻时间
schedule.every().monday.do(func)
#每周1，12点开始执行
schedule.every().monday.at("12:00").do(func)
"""
schedule.every(10).minutes.do(job)               # 每隔 10 分钟运行一次 job 函数
schedule.every().hour.do(job)                    # 每隔 1 小时运行一次 job 函数
schedule.every().day.at("10:30").do(job)         # 每天在 10:30 时间点运行 job 函数
schedule.every().monday.do(job)                  # 每周一 运行一次 job 函数
schedule.every().wednesday.at("13:15").do(job)   # 每周三 13：15 时间点运行 job 函数
schedule.every().minute.at(":17").do(job)        # 每分钟的 17 秒时间点运行 job 函数
"""
