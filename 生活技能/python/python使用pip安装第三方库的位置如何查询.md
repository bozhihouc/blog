# python使用pip安装第三方库的位置如何查询
`@Time   : 2021/5/14 下午1:40`
`@Author : 852782749@qq.com`


```
开始编辑～
```
```
最近又拾起来了渗透，今天在尝试注入的时候，系统过滤的空格，
经手工验证，可以使用 /*任意字符*/ 进行绕过，
一点点去测试注入点有点头昏脑胀，就丢在了sqlmap，一直没有找到sqlmap的tamper插件位置，
因为电脑里面使用的sqlmap是使用python pip install sqlmap进行安装的，
一直找不到python的site-packages位置，
又是PyCharm工具的[File -> Other Settings-> Preferences for New Projects -> Project Interpreter ]，
又是find，都没有找对位置，

还是格局太小啊……


pip在安装第三方库时，如果安装的库是存在的，那么会出现提示告警信息，
    如，在某某位置存在xxx版本的第三方库，安装结束等信息

格局还是要提升啊

```



> 乾坤未定，你我皆是黑马