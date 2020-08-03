# Tomcat自启动
`@Time   : 2020/8/3 13:16`
`@Author : 852782749@qq.com`


```
开始编辑～
```

### 配置JAVA_HOME
```angular2html
JAVA_HOME C:\Java\jdk1.8.0_251
```

### 配置 CATALINA_HOME
```angular2html
这台电脑->属性->高级配置->环境变量
用户变量
CATALINA_HOME
C:\apache-tomcat-7.0.69\bin
```
### 配置path
```angular2html
path
%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;%CATALINA_HOME%\bin;
```
### 配置服务
```angular2html
service.bat install/remove
```
![](images\tomcat_01.png)


> 乾坤未定，你我皆是黑马