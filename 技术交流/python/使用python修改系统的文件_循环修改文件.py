#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020年5月26日, 0026 14:07
# @Author  : 862897316@qq.com
# @File    : 使用python修改系统的文件_循环修改文件.py
# @Software: PyCharm

import re
import time

def xieru():
    old_file = '1.html'
    fopen = open(old_file, 'r')
    old_str = '<script language="JavaScript" src="123.js"></script>'
    print(old_str)
    w_str = ""
    new_str = '<script language="JavaScript" src="123.js"></script>\n<script language="JavaScript" src="http://www.baidu.com/123.js"></script>'
    for line in fopen:
        if re.search('baidu', line):
            print('jhhh')
        else:
            line = re.sub(old_str, new_str, line)
            w_str += line
    print(w_str)
    wopen = open(old_file, 'w')
    wopen.write(w_str)
    wopen.close()
    fopen.close()
if __name__ == '__main__':
    for i in range(99):
        xieru()
        time.sleep(19)