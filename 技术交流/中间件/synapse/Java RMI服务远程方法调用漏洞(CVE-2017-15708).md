# Java RMI 服务远程方法调用漏洞(CVE-2017-15708)


```
环境：Windows server 2008
jdk:1.6.0_45
synapse 2.1.0
https://mirrors.tuna.tsinghua.edu.cn/apache/synapse/2.1.0/synapse-2.1.0-bin.zip

```

### 修改配置文件``wrapper.conf``
```angular2html
C:\synapse-2.1.0\repository\conf\wrapper.conf
```
#### 修改``Java Application``
````angular2html
# Java Application
#wrapper.java.command=java
wrapper.java.command=C:\Java\jdk1.6.0_45\bin\java.exe
````
### 然后通过 ``C:\synapse-2.1.0\bin``下的脚本启动服务或者安装服务
```angular2html
native
ciphertool.bat
ciphertool.sh
install-synapse-service.bat     //Windows 安装服务
synapse-config-migrator.sh
synapse-daemon.sh
synapse.bat                     //Windows 启动服务
synapse.sh
uninstall-synapse-service.bat
```

> 如果安装没有问题，就可以使用服务设置开机自启
>
> 注意，最重要的就是`native`的配置文件`wrapper.conf`,因为启动的时候是从这里获取java的版本的
>
>并且，在`jdk1.8`里面已经修复了rmi，所以选择了`jdk1.6`进行测试