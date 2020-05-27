# Docker启动

### 启动容器
```angular2html
docker run -dit -p8001:80 -p8022:22 -p8006:3306 image_ID /bin/bash
```
### 查看启动状态
```angular2html
docker ps
```
### 进入容器shell

```angular2html
docker exec -it 容器ID /bin/bash
```
