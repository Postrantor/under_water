#! /usr/bin/env python
# -*- coding:utf-8 -*-

import serial
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
        val = os.popen(cmd).read()  # 执行结果包含在val中os.popen

        return val

    def port_list(self):
        port_list = list(serial.tools.list_ports.comports())
        # print(port_list)
        if len(port_list) == 0:
            print('None Port')
        else:
            for i in range(0, len(port_list)):
                print(port_list[i])

    def port_info(self):
        cmd = 'udevadm info /dev/ttyUSB4'
        # cmd = 'lsusb'
        cmd = 'll /dev | grep ttyUSB'  # 这个貌似需要单独运行
        cmd_result = self.popen_cmd(cmd)
        print(cmd_result)

    def port_state(self):
        port = serial.Serial(
            '/dev/UCR_Coulomb',  # 获取当前usb端口: `python -m serial.tools.list_ports`
            baudrate=115200,  # 波特率, 例如：50,75,110,134,150,200,300,600,1200,1800,2400,4800,9600,19200,38400,57600,115200
            # parity=serial.PARITY_EVEN,
            # stopbits=serial.STOPBITS_ONE,
            # bytesize=serial.SEVENBITS, # 该处会使编码发生变化，需要注释
            timeout=.1,  # 超时设置，None = 永远等待操作；0 = ；立即返回请求结果；Num(其他数值) = 等待时间(s)
            # xonxoff=0 # 软件流控
        )
        print('Port`s name:     ' + str(port.portstr))  # 当前串口
        print('Port`s baudrate: ' + str(port.baudrate))  # 获取波特率
        print('Port is open:    ' + str(port.isOpen()))
        print('Port is readable:' + str(port.readable()))


def main():
    port = PortList()
    # port.port_info()
    port.port_list()
    port.port_state()


if __name__ == "__main__":
    main()
