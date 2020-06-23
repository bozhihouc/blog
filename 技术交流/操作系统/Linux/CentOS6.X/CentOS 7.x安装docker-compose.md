# CentOS 7安装docker-compose

###使用yum安装docker-compose时提示没有这个包

```angular2html
可以使用两个命令安装
第一个
更新yum源
sudo yum -y install epel-release
然后安装pip
sudo yum -y install python-pip
使用pip安装docker-compose

第二个
更新yum源
sudo yum -y install epel-release
然后可以直接安装
yum install docker-compose
```
