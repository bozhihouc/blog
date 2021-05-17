# 解决burpsuite大量Firefox浏览器请求success.txt
`@Time   : 2021/5/17 下午3:33`
`@Author : 852782749@qq.com`


```
开始编辑～
```

### 第一步 
```angular2html
打开 firefox 浏览器，在地址栏输入：about:config
```
### 第二步
```angular2html
在搜索框“Search”输入：network.captive-portal-service.enabled
```
### 第三步
```angular2html
设置布尔值：false
双击可以修改成 false ，或手动修改
```


> 乾坤未定，你我皆是黑马