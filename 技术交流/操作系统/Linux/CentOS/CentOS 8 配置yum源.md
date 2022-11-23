# CentOS 8 配置yum源

`@Time   : 2022/11/23 11:22`
`@Author : 852782749@qq.com`

```
开始编辑～
```
### 备份现有的yum源配置文件
```angular2html
cp -r /etc/yum.repos.d /etc/yum.repos.d.bak
```
### 修改`CentOS-AppStream.repo`、`CentOS-Base.repo`和`CentOS-Extras.repo`
> 修改`CentOS-AppStream.repo`为以下内容
```angular2html
[AppStream]

name=CentOS-$releasever- AppStream

baseurl=http://mirrors.aliyun.com/centos/$releasever/AppStream/$basearch/os/

gpgcheck=1

enabled=1

gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-Official
```

> 修改`CentOS-Base.repo`为以下内容
```angular2html
[BaseOS]

name=CentOS-$releasever- Base

baseurl=http://mirrors.aliyun.com/centos/$releasever/BaseOS/$basearch/os/

gpgcheck=1

enabled=1

gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-Official
```

> 修改`CentOS-Extras.repo`为以下内容
```angular2html
[extras]

name=CentOS-$releasever- Extras

baseurl=http://mirrors.aliyun.com/centos/$releasever/extras/$basearch/os/

gpgcheck=1

enabled=1

gpgkey=http://mirrors.aliyun.com/centos/RPM-GPG-KEY-CentOS-Official
```

### 刷新yum源缓存，使新的yum源配置生效，分别执行下列两条命令
> `yum clean all`
> 
> `yum makecache`

> 乾坤未定，你我皆是黑马