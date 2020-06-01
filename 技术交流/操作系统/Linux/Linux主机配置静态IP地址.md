# Linux主机配置静态IP地址

#### 查找网络配置文件
````angular2html
auto eth0 #开机自动连接网络
iface eth0 inet static #static表示使用固定ip，dhcp表述使用动态ip
address 192.168.1.168 #设置ip地址
netmask 255.255.255.0 #设置子网掩码
gateway 192.168.1.1 #设置网关
````
