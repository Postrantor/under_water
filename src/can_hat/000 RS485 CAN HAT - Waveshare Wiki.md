> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.waveshare.net](https://www.waveshare.net/wiki/RS485_CAN_HAT)

<table><tbody><tr><td colspan="2"><table><tbody><tr><td><b>RS485 CAN HAT</b></td></tr><tr><td><a href="http://www.waveshare.net/shop/RS485-CAN-HAT.htm" title="RS485 CAN HAT" target="_blank" rel="nofollow"><img class="" src="https://www.waveshare.net/w/upload/thumb/9/9f/RS485-CAN-HAT-intro.jpg/360px-RS485-CAN-HAT-intro.jpg"></a></td></tr></tbody></table></td></tr><tr><td colspan="2"><table><tbody><tr><td></td><td></td><th colspan="2">基本信息</th><td></td><td></td></tr><tr><th colspan="3">分类：</th><td colspan="3">树莓派扩展板</td></tr><tr><th colspan="3">功能：</th><td colspan="3">485 总线 CAN 总线</td></tr><tr><th colspan="3">品牌：</th><td colspan="3">Waveshare</td></tr></tbody></table></td></tr><tr><td colspan="2"><table><tbody><tr><td></td><td></td><th colspan="2">板载接口</th><td></td><td></td></tr><tr><td colspan="6"><table><tbody><tr><td><small><b><a href="https://www.waveshare.net/wiki/Category:RPi%E6%8E%A5%E5%8F%A3" title="Category:RPi接口">RPi</a></b></small></td><td><small><b><a href="https://www.waveshare.net/wiki/Category:CAN%E6%8E%A5%E5%8F%A3" title="Category:CAN接口">CAN</a></b></small></td><td><small><b><a href="https://www.waveshare.net/wiki/Category:RS485%E6%8E%A5%E5%8F%A3" title="Category:RS485接口">RS485</a></b></small></td><td><small></small></td></tr><tr><td><small></small></td><td><small></small></td><td><small></small></td><td><small></small></td></tr><tr><td><small></small></td><td><small></small></td><td><small></small></td><td><small></small></td></tr><tr><td><small></small></td><td><small></small></td><td><small></small></td><td><small></small></td></tr><tr><td><small></small></td><td><small></small></td><td><small></small></td><td><small></small></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td colspan="2"><table><tbody><tr><td></td><td></td><th colspan="2">相关产品</th><td></td><td></td></tr><tr><td colspan="6"><table><tbody><tr><th></th></tr><tr><th><table><tbody></tbody></table></th></tr></tbody></table></td></tr></tbody></table></td></tr></tbody></table>

RS485 CAN HAT 是微雪电子为树莓派开发的一款的带 RS485 和 CAN 通信功能的扩展板，具备 RS485、CAN 通信功能。

## 特点

- 基于 Raspberry Pi 40pin GPIO 接口，适用于 Raspberry Pi 系列主板
- 具备 CAN 功能，使用 SPI 接口 CAN 控制器 MCP2515，搭配收发器 SN65HVD230
- 具备 RS485 功能，使用 UART 控制，半双工通讯，收发器为 SP3485
- 板载 TVS(瞬态电压抑制管)，RS485 通讯可有效抑制电路中的浪涌电压和瞬态尖峰电压，防雷防静电
- 预留控制接口，方便其他控制器控制
- 提供完善的配套资料手册 (提供 wiringPi 与 python 例程)

## 产品参数

- 工作电压： 3.3V
- CAN 控制芯片： MCP2515
- CAN 收发器： SN65HVD230
- 485 收发器： SP3485
- 产品尺寸： 65mmx30mm
- 固定孔通经： 3.0mm

## 接口说明

- CAN 总线

<table><tbody><tr><td>功能引脚</td><td>树莓派接口（BCM）</td><td>描述</td></tr><tr><td>3V3</td><td>3V3</td><td>3.3V 电源正</td></tr><tr><td>GND</td><td>GND</td><td>电源地</td></tr><tr><td>SCK</td><td>SCK</td><td>SPI 时钟输入</td></tr><tr><td>MOSI</td><td>MOSI</td><td>SPI 数据输入</td></tr><tr><td>MISO</td><td>MISO</td><td>SPI 数据输出</td></tr><tr><td>CS</td><td>CE0</td><td>数据 / 命令选择</td></tr><tr><td>INT</td><td>25</td><td>中断输出</td></tr></tbody></table>

- RS485 总线

<table><tbody><tr><td>功能引脚</td><td>树莓派接口（BCM）</td><td>描述</td></tr><tr><td>3V3</td><td>3V3</td><td>3.3V 电源正</td></tr><tr><td>GND</td><td>GND</td><td>电源地</td></tr><tr><td>RXD</td><td>RXD</td><td>串口接收</td></tr><tr><td>TXD</td><td>TXD</td><td>串口发送</td></tr><tr><td>RSE</td><td>4</td><td>设置收发</td></tr></tbody></table>

对于 RSE 引脚，可以选择不使用，模块出厂默认使用的是硬件自动接收与发送。

## 硬件说明

### CAN 总线

CAN 模块的功能是处理所有 CAN 总线上的报文接收和发送。报文发送时，首先将报文装载到正确的报文缓冲器和控制寄存器中。通过 SPI 接口设置控制寄存器中的相应位或使用发送使能引脚均可启动发送操作。通过读取相应的寄存器可以检查通讯状态和错误。 会对在 CAN 总线上检测到的任何报文进行错误检查，然后与用户定义的滤波器进行匹配，以确定是否将报文移到两个接收缓冲器中的一个。  
由于树莓派本身并不支持 CAN 总线，因此使用 SPI 接口的 CAN 控制器，搭配一个收发器完成 CAN 功能。  
Microchip 的 MCP2515 是一款 CAN 协议控制器，完全支持 CAN V2.0B 技术规范。该器件能发送和接收标准和扩展数据帧以及远程帧。 MCP2515 自带的两个验收屏蔽寄存器和六个验收滤波寄存器可以过滤掉不想要的报文，因此减少了主单片机（MCU）的开销。MCU 通过 SPI 接口与该器件连接, 即树莓派通过 SPI 接口连接芯片，对于树莓派使用该芯片不需要编写驱动，只需要打开设备树中的内核驱动即可使用。  
[![](https://www.waveshare.net/w/upload/6/61/RS485_CAN_HAT_MCP2515.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_MCP2515.png)  
更多详细请参考数据手册；  
SN65HVD230 是德州仪器公司生产的 3.3V CAN 收发器，该器件适用于较高通信速率、良好抗干扰 能力和高可靠性 CAN 总线的串行通信。SN65HVD230 具有高速、斜率和等待 3 种不同的工作模式。 其工作模式控制可通过 Rs 控制引脚来实现。CAN 控制器的输出引脚 Tx 接到 SN65HVD230 的数据 输入端 D，可将此 CAN 节点发送的数据传送到 CAN 网络中；而 CAN 控制器的接收引脚 Rx 和 SN65HVD230 的数据输出端 R 相连，用于接收数据。  
[![](https://www.waveshare.net/w/upload/4/42/RS485_CAN_HAT_SN65HVD230.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_SN65HVD230.png)

### RS485 总线

SP3485 接口芯片是一种 RS-485 驱动芯片。用于 RS-485 通信的低功耗收发器。 采用单一电源 + 3.3V 工作，采用半双工通讯方式。RO 和 DI 端分别为接收器的输出和驱动器的输入端；(RE) ̅ 和 DE 端分别为接收和发送的使能端，当 (RE) ̅ 为逻辑 0 时，器件处于接收状态；当 DE 为逻辑 1 时，器件处于发送状态；A 端和 B 端分别为接收和发送的差分信号端，当 A-B>+0.2V 时，RO 输出逻辑 1；当 A-B<-0.2V 时，RO 输出逻辑 0。A 和 B 端之间加匹配电阻，一般可选 100Ω 的电阻。  
[![](https://www.waveshare.net/w/upload/b/b4/RS485_CAN_HAT_485.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_485.png)  
其中：SP3485 芯片的 RE 与 DE 管脚是设置接收与发送；  
本模块默认的出厂设置是采用硬件自动的收发，也可以选择软件上控制管脚来选择发送与接收，可以通过焊接板上的 0 欧姆电阻来选择控制方式。  
硬件自动控制：  
[![](https://www.waveshare.net/w/upload/f/f9/RS485_CAN_HAT_485SR.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_485SR.png)  
**数据接收**：P_TX 此时为高电平, 为休闲状态。这时候三级管导通，SP3485 芯片的 RE 引脚为低电平，数据接收使能，RO 开始接收数据，将 485AB 口接受到的数据传到 MCU。  
**数据发送**：P_TX 会有一个下拉的电平，表示开始发送数据，此时三极管截止，DE 引脚为高电平，数据发送使能。此时，如果发送的数据为‘1’的时候，三极管会处于导通，虽然接收会变为有效状态但由于芯片在发送阶段时是高阻状态，所以还是保持发送状态，正常传输‘1’。  
注意：使用自动收发由于三级管的通断的速度问题，会导致自动收发的波特率无法做到太高，如果需要很高的波特率建议使用收动收发。

## 安装库

- 安装 BCM2835， 打开树莓派终端，并运行以下指令

```
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
tar zxvf bcm2835-1.60.tar.gz
cd bcm2835-1.60/
sudo ./configure && sudo make && sudo make check && sudo make install
# 更多的可以参考官网：http://www.airspayce.com/mikem/bcm2835/
```

- 安装 wiringPi

```
sudo apt-get install wiringpi
#对于树莓派2019年5月之后的系统（早于之前的可不用执行），可能需要进行升级：
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v
# 运行gpio -v会出现2.52版本，如果没有出现说明安装出错
```

- python

```
sudo apt-get update
sudo apt-get install python-serial
sudo pip install python-can
```

## 下载例程

在树莓派终端运行：

```
sudo apt-get install p7zip-full
wget http://www.waveshare.net/w/upload/d/de/RS485_CAN_HAT_Code.7z
7z x RS485_CAN_HAT_Code.7z -r -o./RS485_CAN_HAT_Code
sudo chmod 777 -R RS485_CAN_HAT_Code/
```

## CAN 使用

本演示程序使用了两个树莓派以及两个 RS485 CAN HAT 模块  
提供 python 与 c 语言程序

### 前置工作

将模块插在树莓派上，然后修改开机脚本 config.txt

```
sudo nano /boot/config.txt
```

在最后一行加入如下：

```
dtparam=spi=on
dtoverlay=mcp2515-can0,oscillator=12000000,interrupt=25,spimaxfrequency=2000000
```

其中 oscillator=12000000，是板载的晶振大小 12M，如下图  
[![](https://www.waveshare.net/w/upload/d/d2/RS485_CAN_HAT_cry12.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_cry12.png)

- 如果购买日期早于 2019 年 8 月份，请使用下面的：

如图，红色框内为 8M 的晶振  
[![](https://www.waveshare.net/w/upload/b/b1/RS485_CAN_HAT_cry.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_cry.png)

```
dtparam=spi=on
dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=25,spimaxfrequency=1000000
```

保存退出后，重启树莓派：

```
sudo reboot
```

重启后，运行命令查看是否初始化成功：

```
dmesg | grep -i '\(can\|spi\)'
```

[![](https://www.waveshare.net/w/upload/thumb/d/d1/RS485_CAN_HAT_CAN1.png/600px-RS485_CAN_HAT_CAN1.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_CAN1.png)  
如果不接上模块可能提示如下：  
[![](https://www.waveshare.net/w/upload/thumb/3/35/RS485_CAN_HAT_CAN2.png/600px-RS485_CAN_HAT_CAN2.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_CAN2.png)  
请检查是否连接上模块。是否开启 SPI 并开启 MCP2515 内核驱动。是否进行重启。  
确定好两边树莓派都这样处理了，把两个模块的 H 与 L 对应连接  
如果使用的是其他的 CAN 设备，确定连线 H-H,L-L 即可

### C

- 阻塞接收，树莓派打开终端，运行：

```
cd RS485_CAN_HAT_Code/CAN/wiringPi/receive/
make clean
make
sudo ./can_receive
```

接收程序是阻塞的，直到读取到数据就结束。  
[![](https://www.waveshare.net/w/upload/thumb/4/49/RS485_CAN_HAT_CAN_reveive.png/600px-RS485_CAN_HAT_CAN_reveive.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_CAN_reveive.png)

- 发送，树莓派打开终端，运行：

```
cd RS485_CAN_HAT_Code/CAN/wiringPi/receive/
make clean
make
sudo ./can_send
```

[![](https://www.waveshare.net/w/upload/thumb/f/fb/RS485_CAN_HAT_CAN_send.png/600px-RS485_CAN_HAT_CAN_send.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_CAN_send.png)

此时接收接收到对应的 id 的报文：  
[![](https://www.waveshare.net/w/upload/thumb/7/79/RS485_CAN_HAT_CAN_reveive1.png/600px-RS485_CAN_HAT_CAN_reveive1.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_CAN_reveive1.png)

### python

树莓派打开终端，运行：

```
cd RS485_CAN_HAT_Code/CAN/python/
#先运行接收：
sudo python can_reveive.py
#发送端：
sudo python can_send.py
```

本演示程序使用了两个树莓派以及两个 RS485 CAN HAT 模块  
提供 python 与 wiringPi 语言程序

### 前置工作

## 开启 Uart 接口

打开树莓派终端，输入以下指令进入配置界面

```
sudo raspi-config
选择Interfacing Options -> Serial，关闭shell访问，打开硬件串口
```

[![](https://www.waveshare.net/w/upload/3/31/L76X_GPS_Module_rpi_serial.png)](https://www.waveshare.net/wiki/File:L76X_GPS_Module_rpi_serial.png)

然后重启树莓派：

```
sudo reboot
```

打开 / boot/config.txt 文件，找到如下配置语句使能串口，如果没有，可添加在文件最后面。

```
enable_uart=1
```

对于树莓派 3B 用户，串口用于蓝牙，需要注释掉：

```
#dtoverlay=pi3-miniuart-bt
```

然后重启树莓派：

```
sudo reboot
```

确定好两边树莓派都这样处理了，把两个模块的 A 与 B 对应连接  
如果使用的是其他的 485 设备，确定连线 A-A,B-B 即可

### C

- 阻塞接收，树莓派打开终端，运行：

```
cd RS485_CAN_HAT_Code/485/WiringPi/send
make clean
make
sudo ./485_receive
```

接收程序是阻塞的，直到读取到数据就结束。  
[![](https://www.waveshare.net/w/upload/thumb/5/50/RS485_CAN_HAT_485_receive.png/600px-RS485_CAN_HAT_485_receive.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_485_receive.png)

- 发送，树莓派打开终端，运行：

```
cd RS485_CAN_HAT_Code/485/WiringPi/send
make clean
make
sudo ./485_send
```

此时接收端接收到程序  
[![](https://www.waveshare.net/w/upload/thumb/6/66/RS485_CAN_HAT_485_receive2.png/600px-RS485_CAN_HAT_485_receive2.png)](https://www.waveshare.net/wiki/File:RS485_CAN_HAT_485_receive2.png)

### python 例程

```
cd RS485_CAN_HAT_Code/485/python/
#先运行接收：
sudo python reveive.py
#发送端：
sudo python send.py
```

### 故障排查

如果 485 通信不正常，请分步调试：

1.  确定树莓派的硬件版本，如果是树莓派 ZERO/3B，则程序中的串口需要修改成 / dev/ttyAMA0；
2.  确定 485 的 A,B 是否与控制的 485 设备 A,B 一一对应；
3.  可以先使用 USB to 485 设备与 RS485 CAN HAT 通信，保证树莓派的设置没有问题；

```
dtoverlay=mcp2515-can0,oscillator=8000000,interrupt=25,spimaxfrequency=1000000
```

<table><tbody><tr><td><b><big>答复:</big></b><br></td></tr><tr><td><p>这是一款入门级的 485 和 CAN，都是不带隔离的。</p></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr></tbody></table>

<table><tbody><tr><td><b><big>答复:</big></b><br></td></tr><tr><td><ol><li>确定树莓派的硬件版本，如果是树莓派 ZERO/3B，则程序中的串口需要修改成 / dev/ttyAMA0；</li><li>检查树莓派的串口通信是否开启了流控；</li><li>确定 485 的 A,B 是否与控制的 485 设备 A,B 一一对应；</li><li>可以先使用 USB to 485 设备与 RS485 CAN HAT 通信，保证树莓派的设置没有问题；</li><li>检察串口通信参数的奇数偶数位校验的设置。</li></ol></td></tr><tr><td></td></tr><tr><td></td></tr><tr><td></td></tr></tbody></table>

EMAIL：3004637648@qq.com  
电话：0755-83040712  
QQ：3004637648  
微信：扫下方二维码添加  
[![](https://www.waveshare.net/w/upload/thumb/4/42/Wkg.jpg/200px-Wkg.jpg)](https://www.waveshare.net/wiki/File:Wkg.jpg)

- 企业微信添加好友时软件无提示，我们无法及时通过客户好友申请。如长时间无响应，请用其他联系方式。  
  说明：添加之后直接留言即可，请勿又发邮箱又加 QQ 又加微信，三者添加一个联系即可。

<table><tbody><tr><td>说明：进行售后服务前，请准备好客户信息（定货单位、定货人等），以供验证。<br></td><td></td></tr></tbody></table>
