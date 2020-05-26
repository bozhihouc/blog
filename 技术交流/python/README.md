# Windows bat脚本隐藏黑框

```angular2bat
@echo off 
if "%1" == "h" goto begin 
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit 
:begin 
```
### 需要执行的命令在后面直接填写，如需要运行python
```angular2html
@echo off 
if "%1" == "h" goto begin 
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit 
:begin 
python c:\修改文件.py
```

### 使用python循环修改某一个文件，需要判断是否存在要修改的内容，不存在就修改
```angular2

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
```
