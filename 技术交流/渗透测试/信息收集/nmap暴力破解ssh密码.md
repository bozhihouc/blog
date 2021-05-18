# nmap 暴力破解SSH密码

### 查询namp script是否存在ssh-brute.nse模块
```angular2
ls -al /usr/share/nmap/scripts |grep ssh
```
### 使用命令
```angular2
namp -p 22 --script=ssh-brute.nse 192.168.1.22
```
