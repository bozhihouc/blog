# docker _ubuntu 容器安装web服务

### 搭建web服务
```angular2html
nginx
php
mysql
```
### ubuntu 安装nginx mysql php
```angular2html
apt-get update
apt-get install apache2 php php-gd php-fpm libapache2-mod-php php-mysql mysql-server

```

### ubuntu 安装网络分析工具包（ifconfig netstat 等）
```angular2html
apt-get install net-tools

```
### ubuntu 查看所有服务
```angular2html
service --status-all
```

### 在物理机安装mysql8.0会提示修改密码，然后安装phpcms没有发现问题
```angular2html
这里测试docker 安装命令行库
apt-get install libncurses5-dev

```
### linux shell 图形编程
```angular2html 实例
#!/bin/bash

whiptail --title "Test Message Box" --msgbox "Create a message box with whiptail. Choose Ok to continue." 10 60

```
### docker 安装其他版本的容器
````angular2html
在网站 https://hub.docker.com/ 搜索需要的容器
在界面点击tags选择相应的版本

如：docker pull ubuntu:16.04

````
