#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    这个是对应的第二家店铺的解算板，持续读取数据
'''

# %% import
import serial
import time
PortID_Coulomb = '/dev/Coulomb'

# UCR_L
# %%


class Port():
    '''
        定义Port类
    '''
    defaultPortID = PortID_Coulomb
    defaultBaud = 115200
    defaultTimeout = 1  # .1

    def __init__(self):
        self.StartSerial()

    def StartSerial(self, baud=defaultBaud, serialPort=defaultPortID, timeout=defaultTimeout):
        '''
            初始化，设置串口通信速率为9600
            超时设置为None就可以，可能是应为这个RS232是全双工的，所以接收和发送的前后脚的
            其他的设置被注释了，应为没用，反而还会有麻烦
        '''
        self.CopleySerial = serial.Serial()
        self.CopleySerial.timeout = timeout
        self.CopleySerial.port = serialPort
        self.CopleySerial.baudrate = baud
        self.CopleySerial.open()

    def RxD(self):
        '''
            调用该函数，写入要传送的ASCII给驱动器
            并使用read_until读取返回的一行数据，以'\r'为终止符
        '''
        print('RxD: ' + self.CopleySerial.read_until('\r')[0:-1])

    def PortInfo(self):
        '''
            输出当前端口的状态
        '''
        print('Port`s name:     ' + str(self.CopleySerial.portstr))  # 当前串口
        print('Port`s baudrate: ' + str(self.CopleySerial.baudrate))  # 获取波特率
        print('Port is open:    ' + str(self.CopleySerial.isOpen()))
        print('Port is readable:' + str(self.CopleySerial.readable()))

    def OutputResult(self):
        while True:
            time.sleep(0.1)
            self.RxD()
            print '--- --- ---'


# %%
def main():
    Ports = Port()  # 创建Port()类
    Ports.OutputResult()


# Program start from here
if __name__ == '__main__':
    main()
