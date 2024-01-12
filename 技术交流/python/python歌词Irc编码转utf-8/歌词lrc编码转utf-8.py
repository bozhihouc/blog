#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/21 上午10:00
# @Author  : 852782749@qq.com
# @File    : 歌词Irc编码转utf-8.py
# @Software: PyCharm
import os
import chardet

def convert_to_utf8(file_path):
    # 读取文件内容
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # 检测文件编码
    encoding = chardet.detect(content)['encoding']

    # 如果检测到的编码不是utf-8，则进行转换
    if encoding and encoding.lower() != 'utf-8':
        try:
            content = content.decode(encoding)
            with open(file_path, 'w') as f:
                f.write(content.encode('utf-8'))
            print("Converted {} from {} to UTF-8".format(file_path, encoding))
        except UnicodeDecodeError:
            print("Failed to decode {} with {} encoding".format(file_path, encoding))

def batch_convert_lrc_to_utf8(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 只处理LRC文件
            if file.endswith('.lrc'):
                file_path = os.path.join(root, file)
                convert_to_utf8(file_path)

# 指定目录，批量转换该目录下所有LRC文件为UTF-8
target_directory = "./"
batch_convert_lrc_to_utf8(target_directory)