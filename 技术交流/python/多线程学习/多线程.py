#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021年1月15日, 0015 14:00
# @Author  : 862597316@qq.com
# @Site    : 
# @File    : 多线程.py
# @Software: PyCharm

from threading import Thread
import time

# 子线程调用函数
def thFunc(i):
    print("线程 %d 启动 ..."%i)
    time.sleep(1)
if __name__ =='__main__':
    print("主线程开始...")
    for i in range(3):
        th = Thread(target=thFunc,args=(i,))
        th.start()
        th.join()
    print("主线程结束")