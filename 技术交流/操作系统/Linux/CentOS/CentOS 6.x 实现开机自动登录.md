# CentOS 6.x 实现开机自动登录

### 开机自动登录设置
打开文件
 `vim /etc/gdm/custom.conf`
```配置文件
# GDM configuration storage 

[daemon]
#默认是没有这两行数据，即，允许自动登录；自动登录的账户为root
AutomaticLoginEnable=true
AutomaticLogin=root

[security]

[xdmcp]

[greeter]

[chooser]

[debug]

```