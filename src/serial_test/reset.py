#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
'''

# %% import
import serial
import time
from copley_lib.ParamDict_EventStatus import BitsMapped as BitsMapped_ES
import copley_lib.CopleyControl as Copley
from methods_lib.kalman_filter import SingleStateKalmanFilter
# %% constant
from constant_lib.Constant_Serial import *


# %% class
class Port():

    def __init__(self):
        self.NodeID = 0
        self.PortID = PortID_UCR
        self.connectSerial()

    def connectSerial(self, baud=defaultBaud, timeout=defaultTimeout):
        self.dev_serial = serial.Serial()
        self.dev_serial.port = self.PortID  # 获取当前usb端口: `python -m serial.tools.list_ports`
        self.dev_serial.timeout = timeout  # 超时设置，None=永远等待操作；0=立即返回请求结果；Num(其他数值)=等待时间(s)
        self.dev_serial.baudrate = baud  # serial port baud rate: 9600(9615) ~ 115200(113636)
        self.openSerialPort()

    def openSerialPort(self):
        try:
            self.dev_serial.open()
        except Exception as result:
            print(result)
            # pass # not need print

    def RxD(self, cmd):
        '''
        调用该函数，写入要传送的ASCII给驱动器，并使用`read_until`读取返回的一行数据，以'\r'为终止符
        '''
        self.dev_serial.write(cmd)
        result = self.dev_serial.read_until('\r')  # [0:-1]
        print('RxD: {}\t{}'.format(cmd[:-1], result))
        return result

    def print_log(self, log='time_msg'):
        if log == 'full_msg':
            msg = '\n\t- PortID: {}\n\t- NodeID: {}\n\t- Buad: {}\n\t- Timeout: {}\n\t- Time: {}'.format(
                self.dev_serial.port, self.NodeID, self.dev_serial.baudrate,
                self.dev_serial.timeout, time.asctime())
        elif log == 'time_msg':
            msg = '\n\t- PortID: {}\n\t- NodeID: {}\n\t- Time: {}'.format(
                self.dev_serial.port, self.NodeID, time.asctime())
        else:
            msg = '\n\t- PortID: {}'.format(self.dev_serial.port)
        return msg

    def Write(self):
        self.RxD('0 s r0x24 0\r')  # 所需的状态参数（0x24）定义了驱动器的操作模式和输入源控制。
        self.RxD('1 s r0x24 0\r')  # 所需的状态参数（0x24）定义了驱动器的操作模式和输入源控制。
        # Feedback
        # self.RxD('enc clear\r')
        # a0 = self.RxD('g r0xa0\r') # Event Status Register(0xA0). Bits: 0~31
        # a1 = self.RxD('g r0xa1\r')
        # a4 = self.RxD('g r0xa4\r')
        # self.RxD('s r0xa4 512\r')
        # print('A0: {}\nA1: {}\nA4: {}'.format(BitsMapped_ES('0xA0', a0[2:]), BitsMapped_ES('0xA0', a1[2:]), BitsMapped_ES('0xA4', a4[2:])))
        # self.RxD('s r0xa1 {}\r'.format(a1[2:]))
        # Encoder
        self.RxD('0 s r0x32 0\r')  # Motor position. Units: counts.
        self.RxD('0 g r0x32\r')
        self.RxD('1 s r0x32 0\r')
        self.RxD('1 g r0x32\r')
        # Baud
        # self.RxD('0 g r0x90\r') # Serial Port Baud Rate. Units: bits/s.
        # self.RxD('0 g r0xc1\r') # CAN Network Node ID Configuration./# 50,000 = 0101 0000 0000 0000
        # self.RxD('1 g r0x90\r') # Serial Port Baud Rate. Units: bits/s.
        # self.RxD('1 g r0xc1\r') # CAN Network Node ID Configuration./# 50,000 = 0101 0000 0000 0000


# %% main
def main():
    ports = Port()
    ports.Write()


if __name__ == '__main__':
    main()
