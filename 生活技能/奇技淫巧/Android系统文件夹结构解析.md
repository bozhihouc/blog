# Android系统文件夹结构解析
` @Time : 2020年11月2日, 0002 17:10`
` @Author  : 862897316@qq.com`
` @Software: PyCharm`

```
开始编写
```
### \system\app

这个里面主要存放的是常规下载的应用程序，可以看到都是以APK格式结尾的文件。在这个文件夹下的程序为系统默认的组件，自己安装的软件将不会出现在这里，而是\data\文件夹中。

### \system\bin

这个目录下的文件都是系统的本地程序，从bin文件夹名称可以看出是binary二进制的程序，里面主要是Linux系统自带的组件，Android手机网就主要文件做下简单的分析介绍：
\system\bin\akmd
\system\bin\am
\system\bin\app_process 系统进程
\system\bin\dalvikvm Dalvik虚拟机宿主
\system\bin\dbus-daemon 系统BUS总线监控
\system\bin\debuggerd 调试器
\system\bin\debug_tool 调试工具
\system\bin\dexopt DEX选项
\system\bin\dhcpcd DHCP服务器
\system\bin\dumpstate 状态抓取器
\system\bin\dumpsys 系统抓取器
\system\bin\dvz
\system\bin\fillup
\system\bin\flash_image 闪存映像
\system\bin\hciattach
\system\bin\hcid HCID内核
\system\bin\hostapd
\system\bin\hostapd_cli
\system\bin\htclogkernel
\system\bin\input
\system\bin\installd
\system\bin\itr
\system\bin\linker
\system\bin\logcat Logcat日志打印
\system\bin\logwrapper
\system\bin\mediaserver
\system\bin\monkey
\system\bin\mountd 存储挂载器
\system\bin\netcfg 网络设置
\system\bin\ping Ping程序
\system\bin\playmp3 MP3播放器
\system\bin\pm 包管理器
\system\bin\qemud QEMU虚拟机
\system\bin\radiooptions 无线选项
\system\bin\rild RIL组件
\system\bin\sdptool
\system\bin\sdutil
\system\bin\service
\system\bin\servicemanager 服务管理器
\system\bin\sh
\system\bin\ssltest SSL测试
\system\bin\surfaceflinger 触摸感应驱动
\system\bin\svc 服务
\system\bin\system_server
\system\bin\telnetd Telnet组件
\system\bin\toolbox
\system\bin\wlan_loader
\system\bin\wpa_cli
\system\bin\wpa_supplicant

### \system\etc
从文件夹名称来看保存的都是系统的配置文件，比如APN接入点设置等核心配置。
\system\etc\apns-conf.xml APN接入点配置文件
\system\etc\AudioFilter.csv 音频过滤器配置文件
\system\etc\AudioPara4.csv
\system\etc\bookmarks.xml 书签数据库
\system\etc\dbus.conf 总线监视配置文件
\system\etc\dhcpcd
\system\etc\event-log-tags
\system\etc\favorites.xml 收藏夹
\system\etc\firmware 固件信息
\system\etc\gps.conf GPS设置文件
\system\etc\hcid.conf 内核HCID配置文件
\system\etc\hosts 网络DNS缓存
\system\etc\init.goldfish.sh
\system\etc\location 定位相关
\system\etc\mountd.conf 存储挂载配置文件
\system\etc\NOTICE.html 提示网页
\system\etc\permissions.xml 权限许可
\system\etc\pvplayer.conf
\system\etc\security
\system\etc\wifi WLAN相关组件
\system\etc\dhcpcd\dhcpcd-hooks
\system\etc\dhcpcd\dhcpcd-run-hooks
\system\etc\dhcpcd\dhcpcd.conf
\system\etc\dhcpcd\dhcpcd-hooks\01-test
\system\etc\dhcpcd\dhcpcd-hooks\20-dns.conf
\system\etc\dhcpcd\dhcpcd-hooks\95-configured
\system\etc\firmware\brf6300.bin
\system\etc\location\gps
\system\etc\location\gps\location 定位相关
\system\etc\location\gps\nmea GPS数据解析
\system\etc\location\gps\properties
\system\etc\security\cacerts.bks
\system\etc\security\otacerts.zip OTA下载验证
\system\etc\wifi\Fw1251r1c.bin
\system\etc\wifi\tiwlan.ini
\system\etc\wifi\wpa_supplicant.conf WPA验证组件

### \system\fonts
字体文件夹，除了标准字体和粗体、斜体外可以看到文件体积最大的可能是中文字库，或一些unicode字库，从T-Mobile G1上可以清楚的看到显示简体中文正常，其中DroidSansFallback.ttf文件大小
\system\fonts\DroidSans-Bold.ttf
\system\fonts\DroidSans.ttf
\system\fonts\DroidSansFallback.ttf
\system\fonts\DroidSansMono.ttf
\system\fonts\DroidSerif-Bold.ttf
\system\fonts\DroidSerif-BoldItalic.ttf
\system\fonts\DroidSerif-Italic.ttf
\system\fonts\DroidSerif-Regular.ttf

### \system\framework
framework主要是一些核心的文件，从后缀名为jar可以看出是是系统平台框架。
\system\framework\am.jar
\system\framework\am.odex
\system\framework\android.awt.jar AWT库
\system\framework\android.awt.odex
\system\framework\android.policy.jar
\system\framework\android.policy.odex
\system\framework\android.test.runner.jar
\system\framework\android.test.runner.odex
\system\framework\com.google.android.gtalkservice.jar GTalk服务
\system\framework\com.google.android.gtalkservice.odex
\system\framework\com.google.android.maps.jar 电子地图库
\system\framework\com.google.android.maps.odex
\system\framework\core.jar 核心库，启动桌面时首先加载这个
\system\framework\core.odex
\system\framework\ext.jar
\system\framework\ext.odex
\system\framework\framework-res.apk
\system\framework\framework-tests.jar
\system\framework\framework-tests.odex
\system\framework\framework.jar
\system\framework\framework.odex
\system\framework\input.jar 输入库
\system\framework\input.odex
\system\framework\itr.jar
\system\framework\itr.odex
\system\framework\monkey.jar
\system\framework\monkey.odex
\system\framework\pm.jar 包管理库
\system\framework\pm.odex
\system\framework\services.jar
\system\framework\services.odex
\system\framework\ssltest.jar
\system\framework\ssltest.odex
\system\framework\svc.jar 系统服务
\system\framework\svc.odex

### \system\lib
lib目录中存放的主要是系统底层库，如平台运行时库。

### \system\media
铃声音乐文件夹，除了常规的铃声外还有一些系统提示事件音

### \system\sounds
默认的音乐测试文件，仅有一个test.mid文件，用于播放测试的文件。
\system\sounds\test.mid

### \system\usr
用户文件夹，包含共享、键盘布局、时间区域文件等。

整个Android平台的文件不止是这么多，部分文件在/data文件夹中都是用户文件夹




> 乾坤未定,你我皆是黑马