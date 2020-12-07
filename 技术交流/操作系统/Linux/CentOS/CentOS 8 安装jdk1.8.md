# CentOS 8 安装jdk1.8
` @Time : 2020年12月7日, 0007 15:39`
` @Author  : 862897316@qq.com`
` @Software: PyCharm`

```
开始编写
```
### 下载地址
```https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html```

### 查看新系统是否安装java环境

```angular2html
yum list installed |grep java
```
### 卸载软件命令

```angular2html
rpm -e –nodeps 软件包名称
```
### 安装jdk
#### 解压tar文件
```angular2html
tar -zxvf jdk-8u271-linux-x64.tar.gz
```

#### 移动至`/usr/local`
```angular2html
mv jdk1.8.0_271/ /usr/local/
```

### 配置环境变量
#### 编辑`/etc/profile`文件，并键入`G`到达文件末行
```angular2html
vim /etc/profile
```
#### 在末行添加如下内容
```angular2html
JAVA_HOME=/usr/local/jdk1.8.0_271
JRE_HOME=/usr/local/jdk1.8.0_271/jre
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
export JAVA_HOME JRE_HOME PATH CLASSPATH
```
#### 使用命令`source /etc/profile`使配置生效

### 验证`jdk`是否安装成功
```angular2html
[root@localhost ~]# java -version
java version "1.8.0_271"
Java(TM) SE Runtime Environment (build 1.8.0_271-b09)
Java HotSpot(TM) 64-Bit Server VM (build 25.271-b09, mixed mode)

```


> 乾坤未定,你我皆是黑马