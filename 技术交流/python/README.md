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
