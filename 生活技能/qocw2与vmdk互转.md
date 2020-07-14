# qcow2 与 vmdk 互转

### qcow2 转 vmdk
```angular2html
qemu-img convert -f qcow2 centos.qcow2 -O vmdk centos.vmdk
```

### vmdk 转 qcow2

```angular2html
qemu-img convert -f vmdk -O qcow2 centos.vmdk centos.qcow2

```