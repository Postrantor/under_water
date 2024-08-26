#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
    # 列出可用的串口
    # sudo vi /etc/udev/rules.d/
'''

import serial #导入模块
import serial.tools.list_ports
import os

class PortList():
    """
    docstring
    """
    def popen_cmd(self, cmd):
        """
        popen模块执行linux命令。返回值是类文件对象，获取结果要采用read()或者readlines()
        :return:
        """
        val = os.popen(cmd).read() # 执行结果包含在val中os.popen

        return val

    def port_list(self):
        port_list = list(serial.tools.list_ports.comports())
        # print(port_list)
        if len(port_list) == 0:
            print('None Port')
        else:
            for i in range(0,len(port_list)):
                print(port_list[i])

    def port_info(self):
        cmd = 'udevadm info /dev/ttyUSB4'
        # cmd = 'lsusb'
        cmd = 'll /dev | grep ttyUSB' # 这个貌似需要单独运行
        cmd_result = self.popen_cmd(cmd)
        print(cmd_result)

    def port_state(self):
        port =serial.Serial(
            '/dev/UCR_Coulomb', # 获取当前usb端口: `python -m serial.tools.list_ports`
            baudrate=115200, # 波特率, 例如：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
            # parity=serial.PARITY_EVEN,
            # stopbits=serial.STOPBITS_ONE,
            # bytesize=serial.SEVENBITS, # 该处会使编码发生变化，需要注释
            timeout=.1, # 超时设置，None = 永远等待操作；0 = ；立即返回请求结果；Num(其他数值) = 等待时间(s)
            # xonxoff=0 # 软件流控
            )
        print('Port`s name:     ' + str(port.portstr)) # 当前串口
        print('Port`s baudrate: ' + str(port.baudrate)) # 获取波特率
        print('Port is open:    ' + str(port.isOpen()))
        print('Port is readable:' + str(port.readable()))

def main():
    port = PortList()
    # port.port_info()
    port.port_list()
    port.port_state()

if __name__ == "__main__":
    main()


'''
# https://blog.csdn.net/xinmei4275/article/details/88620984
# https://blog.csdn.net/IT8343/article/details/106325866/
# 在/etc/udev/rules.d内创建规则文件，固定端口号；此处采用固定树莓派上USB端口的方式，而不是设备ID，因为两个RS232是一样的设备ID
# 在树莓派4上，USB3.0是第一端口和第二端口(上面的是第一)，USB2.0是第三端口和第四端口(上面的是第三)
# 将主驱动的通讯板子设置为第三端口，辅助驱动的板子为第四端口
# 创建文件`Port_QuadRS232HS.rules`，具体内容如下
```
# 这个是树莓派USB2.0上面端口
ACTION=="add",KERNELS=="1-1.3:1.0",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Drive_L"
ACTION=="add",KERNELS=="1-1.3:1.1",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Drive_R"
ACTION=="add",KERNELS=="1-1.3:1.2",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Sting_L"
ACTION=="add",KERNELS=="1-1.3:1.3",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Coulomb"
# 这个是树莓派USB2.0下面端口
ACTION=="add",KERNELS=="1-1.4:1.0",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Wing_L"
ACTION=="add",KERNELS=="1-1.4:1.1",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Wing_R"
ACTION=="add",KERNELS=="1-1.4:1.2",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Sting_R"
ACTION=="add",KERNELS=="1-1.4:1.3",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="UCR_Retain02"
```
# 创建文件`Port_HL-340.rules`，具体内容如下
```
# 这个是树莓派USB3.0端口上面
# 暂时使用吧，等RS232转TTL小板到了，就添加到USB2.0端口中
ACTION=="add",KERNELS=="1-1.1:1.0",SUBSYSTEMS=="usb",MODE:="0777",SYMLINK+="Coulomb"
```
[Note]:
    内容, KERNELS表示硬件的usb接口名,不同编号,表示不同的usb接口.``
    下面是添加修改了三个USB端口
# 
/1-1.4:1.0/ttyUSB0
/1-1.4:1.1/ttyUSB1
/1-1.4:1.2/ttyUSB2
/1-1.4:1.3/ttyUSB3

/1-1.3:1.0/ttyUSB5
/1-1.3:1.1/ttyUSB6
/1-1.3:1.2/ttyUSB7
/1-1.3:1.3/ttyUSB8

/1-1.1:1.0/ttyUSB4

然后执行：
$ sudo service udev reload
$ sudo service udev restart

/etc/udev/rules.d/20-usb-serial.rules：
KERNEL=="ttyUSB*"MODE="0777"
KERNEL=="ttyS*"MODE="0777"
'''
'''
# 成功，结果如下
ubuntu@ubuntu:~$ ll /dev | grep ttyUSB
lrwxrwxrwx   1 root root           7 Nov 30 03:30 Sting_L -> ttyUSB2
lrwxrwxrwx   1 root root           7 Nov 30 03:30 Sting_R -> ttyUSB6
lrwxrwxrwx   1 root root           7 Nov 30 03:30 UCR_L -> ttyUSB0
lrwxrwxrwx   1 root root           7 Nov 30 03:30 UCR_R -> ttyUSB1
lrwxrwxrwx   1 root root           7 Nov 30 03:30 UCR_Retain01 -> ttyUSB3
lrwxrwxrwx   1 root root           7 Nov 30 03:30 UCR_Retain02 -> ttyUSB7
lrwxrwxrwx   1 root root           7 Nov 30 03:30 Wing_L -> ttyUSB4
lrwxrwxrwx   1 root root           7 Nov 30 03:30 Wing_R -> ttyUSB5
crwxrwxrwx   1 root dialout 188,   0 Nov 30 03:30 ttyUSB0
crwxrwxrwx   1 root dialout 188,   1 Nov 30 03:30 ttyUSB1
crwxrwxrwx   1 root dialout 188,   2 Nov 30 03:30 ttyUSB2
crwxrwxrwx   1 root dialout 188,   3 Nov 30 03:30 ttyUSB3
crwxrwxrwx   1 root dialout 188,   4 Nov 30 03:30 ttyUSB4
crwxrwxrwx   1 root dialout 188,   5 Nov 30 03:30 ttyUSB5
crwxrwxrwx   1 root dialout 188,   6 Nov 30 03:30 ttyUSB6
crwxrwxrwx   1 root dialout 188,   7 Nov 30 03:30 ttyUSB7
'''