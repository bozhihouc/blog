# Windows 安装MySQL5.6教程
` @Time : 2020年7月28日 9:56`

` @Author  : 862897316@qq.com`

` @Software: PyCharm`

```
开始编写
```
### 选择MySQL版本，下载链接如下
``https://dev.mysql.com/downloads/mysql/``

### my.ini文件配置
```angular2html

[mysql]  
# 设置 mysql 客户端默认字符集  
default-character-set=utf8mb4 
 
[mysqld]
basedir = C:\mysql-5.6.49（mysql所在目录）
datadir = C:\mysql-5.6.49\data（mysql所在目录\data）
#设置 3306 端口，不配置默认3306
port = 3306  

# 设置 mysql 的安装目录  
basedir=C:\mysql-5.6.49

# 设置 mysql 数据库的数据的存放目录  
datadir=C:\mysql-5.6.49\data 

# 允许最大连接数  
max_connections=200  

# 服务端使用的字符集默认为 8 比特编码的 latin1 字符集  
character-set-server=utf8mb4  

# 创建新表时将使用的默认存储引擎  
default-storage-engine=INNODB

```

### 安装mysql服务

```angular2html
cd C:\mysql-5.6.49\bin
执行
mysqld --initialize-insecure --user=mysql

mysqld install

返回
Service successfully installed.
说明安装成功
可以使用 net start/stop mysql 启/停服务
```

> 乾坤未定,你我皆是黑马