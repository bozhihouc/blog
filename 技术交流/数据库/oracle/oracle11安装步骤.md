# oracle11 安装


## 安装JDK
> 我选择的是1.8_251版本的jdk `jdk-8u251-windows-x64.exe`
> 
> 如下图所示，在C盘创建jdk和jre的目录（也可以选择默认安装）

![](images\java1.8_251_01.png)
![](images\java1.8_251_02.png)

> 修改成创建的目录

![](images\java1.8_251_03.png)
> 安装完成

![](images\java1.8_251_04.png)

### 下载链接
```angular2html
https://www.oracle.com/database/technologies/112010-win64soft.html
```
### 客户端连接程序
```angular2html
win64_11gR2_client.zip
```
### 安装包需要将两个压缩到一个文件夹下，双击`setup.exe`运行安装程序

> 如果没有将两个包压缩到一起，会在安装时提示找不到某些文件，导致安装出错

```angular2html
win64_11gR2_database_1of2.zip
win64_11gR2_database_2of2.zip
```
> 如图，将两个database都压缩到了桌面的database目录

![](images\oracle11_01.png)

![](images\oracle11_02.png)
### 运行程序之后，需要等待片刻，才会进入下面的步骤，选择 `是`继续安装
![](images\oracle11_03.png)


> 配置安全更新，如下图操作，不填写邮箱，并去掉勾选

![](images\oracle11_04.png)
> 配置安全更新，如下图操作，不填写邮箱，并去掉勾选

![](images\oracle11_05.png)
> 安装选项，选择 `创建和配置数据库`

![](images\oracle11_06.png)
> 系统类,选择 `桌面类` 即可

![](images\oracle11_07.png)
> 典型安装

![](images\oracle11_08.png)

![](images\oracle11_09.png)

> 点击 `完成` ,等待安装完成即可

![](images\oracle11_10.png)

![](images\oracle11_11.png)
> 安装完成

![](images\oracle11_12.png)
> 可以点击 `口令管理`设置密码

![](images\oracle11_13.png)


