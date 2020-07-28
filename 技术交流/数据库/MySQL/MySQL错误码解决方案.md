# MySQL错误码解决方案
`@Time   : 2020/7/28 14:09`
`@Author : 852782749@qq.com`


```
开始编辑～
```
### MySQL ERROR 1451 23000 外键异常处理
```angular2html
mysql> delete from users;
ERROR 1451 (23000): Cannot delete or updatea parent row
```
### 原因：表有外键所以delete报错了，这里有2种办法处理：
```angular2html
临时设置外键失效
删除表涉及到的外键的表的数据
```
### 外键失效的处理方案
```angular2html
mysql> SET FOREIGN_KEY_CHECKS = 0;  # 临时设置外键失效
Query OK, 0 rows affected (0.00 sec)

mysql> delete from JBPM4_EXECUTION;  #执行删除操作
Query OK, 110 rows affected (0.00 sec)

mysql> SET FOREIGN_KEY_CHECKS = 1;  # 操作结束后恢复外键
Query OK, 0 rows affected (0.00 sec)

```


> 乾坤未定，你我皆是黑马