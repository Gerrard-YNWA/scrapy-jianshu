#!/bin/python
#-*-coding:utf8-*-

import os 
import time
import sched

schedule = sched.scheduler ( time.time, time.sleep )

def func():
    print "triger."
    os.system("scrapy crawl homepage")
def perform1(inc):
    schedule.enter(inc,0,perform1,(inc, ))
    func()    
def mymain():
    #一个小时抓一次
    schedule.enter(0,0,perform1,(3600, ))

if __name__=="__main__":
    mymain()
    schedule.run() 
