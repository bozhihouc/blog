#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021年1月15日, 0015 14:18
# @Author  : 862597316@qq.com
# @Site    : 
# @File    : 多线程模拟彩票发行.py
# @Software: PyCharm

import threading,queue,random
# 定义线程类
class MyThread(threading.Thread):
    # 重写构造方法
    def __init__(self,cpfx_q,i,zjhm,lock):
        super(MyThread,self).__init__()             # 调用父类构造函数
        self.cpfx_q = cpfx_q
        self.i = i
        self.zjhm = zjhm
    # 重写run()方法
    def run(self):
        lock.acquire()
        zjxx = self.cpfx_q.get()
        cphmList = self.cpfx_q.get()
        cphm = random.choice(cphmList)
        cphm_num = cphmList.index(cphm)

        if cphm == self.zjhm:
            zjxx = "抽奖人" + str(self.i) + "号购买的彩票" + str(cphm) + "中奖了！恭喜你"
        cphmList.pop(cphm_num)
        self.cpfx_q.put(zjxx)
        self.cpfx_q.put(cphmList)
        lock.release

if __name__ == '__main__':
    print("…………………………………………………………………彩票开始发行…………………………………………………………………………………")
    cpfx_q = queue.Queue()
    cphmList = list(range(1000,10000))
    random.shuffle(cphmList)
    zjxx = "无人中奖"
    cpfx_q.put(zjxx)
    cpfx_q.put(cphmList)
    zjhm = random.randrange(1000,10000)
    print("本次发行彩票中奖号码：",zjhm)
    lock = threading.Lock()
    for i in range(5000):
        MyThread(cpfx_q,i,zjhm,lock).start()
    print("本次彩票发行结果：",cpfx_q.get())
    print("…………………………………………………………………彩票发行结束…………………………………………………………………………………")
