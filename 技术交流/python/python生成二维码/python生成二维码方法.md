# python生成二维码方法
`@Time   : 2020/12/21 上午9:20`
`@Author : 852782749@qq.com`


```
开始编辑～
```

### 第一种方法
```angular2html
import qrcode

img = qrcode.make('https://www.baidu.com')

with open('test.png','wb') as f:
    img.save(f)

```
### 第二种方法
```angular2html

import qrcode

data = 'https://www.baidu.com'
# 保存文件名称
img_file = r'test1.png'
# 实例化QRCode生成qr对象
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4
)
# 传入数据
qr.add_data(data)
qr.make(fit = True)

# 生成二维码

img = qr.make_image()

# 保存二维码
img.save(img_file)
# 展示二维码
img.show()
```

### 第三种方法

```angular2html
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/21 上午10:00
# @Author  : 852782749@qq.com
# @File    : 二维码.py
# @Software: PyCharm

import qrcode
from PIL import Image
import matplotlib.pyplot as plt
def getQRCode(data,file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=4
    )
    # 添加数据
    qr.add_data(data)
    # 填充数据
    qr.make(fit = True)
    # 生成图片
    img = qr.make_image(fill_color = "green",back_color = "white")

    # 添加logo，打开logo图片
    icon = Image.open("logo.png")
    # 获取图片宽高
    img_w,img_h = img.size
    # 参数设置logo的大小
    factor = 6
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)
    icon_w,icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo尺寸
    icon = icon.resize((icon_w,icon_h), Image.ANTIALIAS)
    # 得到画图的x,y坐标，居中显示
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    # 黏贴logo图片
    img.paste(icon,(w,h),mask = None)
    # 终端显示图片
    plt.imshow(img)
    plt.show()
    # 保存二维码
    img.save(file_name)
    return img

if __name__ == '__main__':
    getQRCode("醉里挑灯看剑，梦回吹角连营。八百里分麾下炙，五十弦翻塞外声，沙场秋点兵。"
              "马作的卢飞快，弓如霹雳弦惊。了却君王天下事，赢得生前身后名。可怜白发生！",'test3.png')
```


### 注意
> 全部使用python3.8
> 
> 在3.8种PTL库换成了pillow，但是引用的名称还是PIL，

> 乾坤未定，你我皆是黑马