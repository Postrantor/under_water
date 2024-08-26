---
title: set serial port
date: 2024-08-26 20:47:17
url:
  [](https://blog.csdn.net/xinmei4275/article/details/88620984)
  [](https://blog.csdn.net/IT8343/article/details/106325866/)
---

## 查看串口信息

```bash
pip install serial
python -m serial.tools.list_ports
```

```bash
lsusb
udevadm info /dev/ttyUSB0
ll /dev | grep ttyUSB
```

## 设置串口映射规则

在 "/etc/udev/rules.d" 内创建规则文件，固定端口号。

创建文件 "/etc/udev/rules.d/20-usb-serial.rules" 并添加

```bash
KERNEL=="ttyUSB*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6001", MODE:="0777", SYMLINK+="rplidar"
```

其中，`idVendor` 和 `idProduct` 通过 `lsusb` 可查询（ID 字段）：

```log
> lsusb

  Bus 001 Device 002: ID 0403:6001 Future Technology Devices International, Ltd FT232 USB-Serial (UART) IC
  Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

`rplidar` 为固定名

重新加载配置文件：

```bash
service udev reload
service udev restart
```

设置之后重新拔插外设即可

## 设置串口可执行权限

修改 "/etc/udev/rules.d/20-usb-serial.rules"：

```bash
KERNEL=="ttyUSB*"MODE="0777"
KERNEL=="ttyS*"MODE="0777"
```

需重新加载配置文件

## 示例 2

```
ACTION=="add",KERNELS=="1-1.1:1.0",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="unitree_fl_legged"
```

## 示例 1

> [Note]:
> 内容, KERNELS 表示硬件的 usb 接口名,不同编号,表示不同的 usb 接口.
> 下面是添加修改了三个 USB 端口

```
> lsusb

/1-1.4:1.0/ttyUSB0
/1-1.4:1.1/ttyUSB1
/1-1.4:1.2/ttyUSB2
/1-1.4:1.3/ttyUSB3

/1-1.3:1.0/ttyUSB5
/1-1.3:1.1/ttyUSB6
/1-1.3:1.2/ttyUSB7
/1-1.3:1.3/ttyUSB8
```

```bash
# 这个是树莓派 USB2.0 上面端口
ACTION=="add",KERNELS=="1-1.3:1.0",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Drive_L"
ACTION=="add",KERNELS=="1-1.3:1.1",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Drive_R"
ACTION=="add",KERNELS=="1-1.3:1.2",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Sting_L"
ACTION=="add",KERNELS=="1-1.3:1.3",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Coulomb"

# 这个是树莓派 USB2.0 下面端口
ACTION=="add",KERNELS=="1-1.4:1.0",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Wing_L"
ACTION=="add",KERNELS=="1-1.4:1.1",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Wing_R"
ACTION=="add",KERNELS=="1-1.4:1.2",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Sting_R"
ACTION=="add",KERNELS=="1-1.4:1.3",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Retain02"
```

# 创建文件`Port_HL-340.rules`，具体内容如下

```bash
# 这个是树莓派 USB3.0 端口上面
# 暂时使用吧，等 RS232 转 TTL 小板到了，就添加到 USB2.0 端口中
ACTION=="add",KERNELS=="1-1.1:1.0",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="Coulomb"
```

然后执行：

```bash
service udev reload
service udev restart
```

"/etc/udev/rules.d/20-usb-serial.rules"：

```bash
KERNEL=="ttyUSB*"MODE="0777"
KERNEL=="ttyS*"MODE="0777"
```

### 成功，结果如下

```bash
$ ll /dev | grep ttyUSB

lrwxrwxrwx 1 root root 7 Nov 30 03:30 Sting_L -> ttyUSB2
lrwxrwxrwx 1 root root 7 Nov 30 03:30 Sting_R -> ttyUSB6
lrwxrwxrwx 1 root root 7 Nov 30 03:30 UCR_L -> ttyUSB0
lrwxrwxrwx 1 root root 7 Nov 30 03:30 UCR_R -> ttyUSB1
lrwxrwxrwx 1 root root 7 Nov 30 03:30 UCR_Retain01 -> ttyUSB3
lrwxrwxrwx 1 root root 7 Nov 30 03:30 UCR_Retain02 -> ttyUSB7
lrwxrwxrwx 1 root root 7 Nov 30 03:30 Wing_L -> ttyUSB4
lrwxrwxrwx 1 root root 7 Nov 30 03:30 Wing_R -> ttyUSB5
crwxrwxrwx 1 root dialout 188, 0 Nov 30 03:30 ttyUSB0
crwxrwxrwx 1 root dialout 188, 1 Nov 30 03:30 ttyUSB1
crwxrwxrwx 1 root dialout 188, 2 Nov 30 03:30 ttyUSB2
crwxrwxrwx 1 root dialout 188, 3 Nov 30 03:30 ttyUSB3
crwxrwxrwx 1 root dialout 188, 4 Nov 30 03:30 ttyUSB4
crwxrwxrwx 1 root dialout 188, 5 Nov 30 03:30 ttyUSB5
crwxrwxrwx 1 root dialout 188, 6 Nov 30 03:30 ttyUSB6
crwxrwxrwx 1 root dialout 188, 7 Nov 30 03:30 ttyUSB7
```
