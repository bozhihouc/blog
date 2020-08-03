# MySQL修改密码的三种方式
` @Time : 2020年8月3日, 0003 10:07`
` @Author  : 862897316@qq.com`
` @Software: PyCharm`

```
开始编写
```

```angular2html
方法1： 用SET PASSWORD命令
　　　　首先登录MySQL，使用mysql自带的那个客户端连接上mysql。
　　　　格式：mysql> set password for 用户名@localhost = password('新密码');
　　　　例子：mysql> set password for root@localhost = password('123');
　　　　
方法2：用mysqladmin （因为我们将bin已经添加到环境变量了，这个mysqladmin也在bin目录下，所以可以直接使用这个mysqladmin功能，使用它来修改密码）

　　　　关于mysqladmin的介绍：是一个执行管理操作的客户端程序。它可以用来检查服务器的配置和当前状态、创建和删除数据库、修改用户密码等等的功能，虽然mysqladmin的很多功能通过使用MySQL自带的mysql客户端可以搞定，但是有时候使用mysqladmin操作会比较简单。
　　　　格式：mysqladmin -u用户名 -p旧密码 password 新密码
　　　　例子：mysqladmin -uroot -p123456 password 123 　
　　　　
方法3：用UPDATE直接编辑那个自动的mysql库中的user表
　　　　首先登录MySQL，连接上mysql服务端。
　　　　mysql> use mysql; use mysql的意思是切换到mysql这个库，这个库是所有的用户表和权限相关的表都在这个库里面，我们进入到这个库才能修改这个库里面的表。
　　　　mysql> update user set password=password('123') where user='root' and host='localhost'; 其中password=password('123') 前面的password是变量，后面的password是mysql提供的给密码加密用的，我们最好不要明文的存密码，对吧，其中user是一个表，存着所有的mysql用户的信息。

　　　　mysql> flush privileges; 刷新权限，让其生效，否则不生效，修改不成功。
```

> 乾坤未定,你我皆是黑马