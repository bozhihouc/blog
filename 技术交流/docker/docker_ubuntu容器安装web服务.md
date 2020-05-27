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
apt-get install apache2 php php-fpm php-mysql mysql-server

```

### ubuntu 安装网络分析工具包（ifconfig netstat 等）
```angular2html
apt-get install net-tools

```
### ubuntu 查看所有服务
```angular2html
service --status-all
```
### mysql8.0版本修改密码(测试未通过)
```angular2html
use mysql;
ALTER user 'root'@'localhost' IDENTIFIED BY 'root'
一直在崩溃
1064（42000）
```