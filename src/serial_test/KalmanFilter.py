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
    '''
    '''
    def __init__(self):
        self.NodeID = 0
        self.PortID = PortID_UCR
        self.connectSerial()
        self.inits_AlgKalmanFilter()
    def inits_AlgKalmanFilter(self):
        # Initialise the Kalman Filter to Current
        A = 1.0 # No process innovation
        C = 1.0 # Measurement
        B = 0.0 # No control input
        Q = 0.001 # Process covariance
        R = 10.0 # Measurement covariance
        x = 0 # Initial estimate
        P = 1.0 # Initial covariance
        self.kf_current = SingleStateKalmanFilter(A, B, C, x, P, Q, R)
    def connectSerial(self, baud=defaultBaud, timeout=defaultTimeout):
        self.dev_serial=serial.Serial()
        self.dev_serial.port=self.PortID # 获取当前usb端口: `python -m serial.tools.list_ports`
        self.dev_serial.timeout=timeout # 超时设置，None=永远等待操作；0=立即返回请求结果；Num(其他数值)=等待时间(s)
        self.dev_serial.baudrate=baud # serial port baud rate: 9600(9615) ~ 115200(113636)
        self.openSerialPort()
    def openSerialPort(self):
        try:
            self.dev_serial.open()
        except Exception as result:
            print(result)
            # pass # not need print
    def RxD(self, cmd):
        '''
            调用该函数，写入要传送的ASCII给驱动器
            并使用read_until读取返回的一行数据，以'\r'为终止符
        '''
        self.dev_serial.write(cmd)
        result = self.dev_serial.read_until('\r')#[0:-1]
        # print('RxD: {}\t{}'.format(cmd[:-1], result))
        return result
    def print_log(self, log='time_msg'):
        if log=='full_msg':
            msg = '\n\t- PortID: {}\n\t- NodeID: {}\n\t- Buad: {}\n\t- Timeout: {}\n\t- Time: {}'.format(self.dev_serial.port, self.NodeID, self.dev_serial.baudrate, self.dev_serial.timeout, time.asctime())
        elif log=='time_msg':
            msg = '\n\t- PortID: {}\n\t- NodeID: {}\n\t- Time: {}'.format(self.dev_serial.port, self.NodeID, time.asctime())
        else:
            msg = '\n\t- PortID: {}'.format(self.dev_serial.port)            
        return msg
    def OutputResult(self):
        num = 0
        while True:
            # time.time_ns()
            num += 1
            if num==1:
                self.RxD('s r0x2f 604858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            if num==200:
                self.RxD('s r0x2f 804858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            if num==400:
                self.RxD('s r0x2f 1004858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            if num==600:
                self.RxD('s r0x2f 1204858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            if num==800:
                self.RxD('s r0x2f 1404858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            if num==1000:
                self.RxD('s r0x2f 1204858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            if num==1200:
                self.RxD('s r0x2f 1004858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            if num==1400:
                self.RxD('s r0x2f 804858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            if num==1600:
                self.RxD('s r0x2f 604858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            if num==1800:
                self.RxD('s r0x2f 0\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
            # print(num)
            # time.sleep(0.1)
            # self.RxD('g r0x18\r') # Actual Velocity. Units: 0.1 encoder counts/s.
            # self.RxD('g r0x17\r') # Actual Position. Units: Counts.
            # self.RxD('g r0x2d \r')

            # self.RxD('g r0x02\r') # Current loop programmed value. Units: 0.01 A.
            current = self.RxD('g r0x18 \r') # Actual Motor Current. Units: 0.01 A.
            current_kf = self.kf_current.step(0, float(current[2:]))
            print("current = {}".format(current[2:]))
            print("current_kf = {}".format(current_kf))
            # self.RxD('g r0x0c\r') # Actual Current, Q axis of rotor space. Units: 0.01 A.

            # a0 = self.RxD('g r0xa0\r') # Event Status Register(0xA0). Bits: 0~31
            # print('A0: {}\n'.format(BitsMapped_ES('0xA0', a0[2:])))
            # print('--- --- ---')
            # time.sleep(0.1)
    def Write(self):
        # if(self.port.isOpen() and self.port.readable()):
        # self.RxD('ok\r'.encode('hex')) # 以hex发送数据('\x6f\x6b\x0d\x0a')
    # 电流模式
        # 在编程的当前模式下启用驱动器。在0.5秒内将输出电流斜坡上升至2A。控制器监视输出电流，达到2 A后，电流将在2秒钟内下降到1A。
        # self.RxD('s r0x6a 1000\r') # Current ramp limit. Units: mA/second.将斜坡速率设置为4 A/s。
        # self.RxD('s r0x02 -20\r') # Programmed current value. Units: 0.01 A. 将输出电平设置为2A。
        # self.RxD('s r0x24 1\r') # 在编程的当前模式下启用驱动器。

        # self.RxD('s r0x6a 500\r') # 将新的斜坡速率设置为0.5 A/s。
        # self.RxD('s r0x02 100\r') # 将输出电平更改为1A。输出电流将以0.5 A/s的速度开始减小。
        # self.RxD('g r0x0c\r') # 读取驱动器的实际电流输出。 示例显示返回的值等于1.50A。
        # self.RxD('s r0x24 0\r') # 禁用驱动器。

        # self.RxD('g r0x38 \r') # Actual Motor Current. Units: 0.01 A.
        # self.RxD('g r0x03\r') # Winding A Current. Units: 0.01 A. Actual current measured at winding A.
        # self.RxD('g r0x04\r') # Winding B Current. Units: 0.01 A. Actual current measured at winding B.
        # self.RxD('g r0x0b\r') # Actual Current, D axis of rotor space. Units: 0.01 A.
        # self.RxD('g r0x0c\r') # Actual Current, Q axis of rotor space. Units: 0.01 A.
    # 速度模式
        # self.RxD('s r0x24 11\r')
        self.RxD('s r0x36 100000\r')
        self.RxD('s r0x37 100000\r')
        self.RxD('s r0x2f 604858\r') # 58709 # 15333 # 15333 # 1rpm # 6048585/5511281
        self.RxD('g r0x18\r') # Actual Velocity. Units: 0.1 encoder counts/s.
        # self.RxD('0 s r0x24 0\r')# 所需的状态参数（0x24）定义了驱动器的操作模式和输入源控制。
        # self.RxD('1 s r0x24 0\r')# 所需的状态参数（0x24）定义了驱动器的操作模式和输入源控制。
    # 位置模式
        # self.RxD('s r0xc8 256\r') # Give trajectory profile mode(0xc8).
        #     # 0     /0 0000 0000 = Absolute move, trapezoidal profile.
        #     # 1     /0 0000 0001 = Absolute move, S-curve profile.
        #     # 256/1 0000 0000 = If set, relative move, trapezoidal profile.
        #     # 257/1 0000 0001 = If clear, relative move, S-curve profile.
        #     # 2    / 0 0000 0010 = Velocity move.
        # self.RxD('s r0xca 176128\r') # Trajectory Generator Position Command(0xca). Units: Counts. 1024*4*86=352256/1000*4*23=92000/1000*4*128=512000
        #    # 117555 = 1000*4*23 * (46/360*10)对于当前右侧，正向是推出
        #    # 27662正值是伸出
        # self.RxD('s r0xcb 3000000\r') # Trajectory Maximum Velocity. Units: 0.1 counts/s. # 8330*1000*4*10/60=5553333
        # self.RxD('s r0xcc 10000\r') # Trajectory Maximum Acceleration. Units: 10 counts/s2. # 1000000差不多就是极限了
        # self.RxD('s r0xcd 10000\r') # Trajectory Maximum Deceleration. Units: 10 counts/s2.
        # # self.RxD('g r0x17\r') # 获取编码器的实际位置，区别于0x2d
        # self.RxD('s r0x24 21\r') # Desired State, Bits: 21 伺服模式下，位置环由轨迹发生器驱动
        # self.RxD('t 1\r')
        self.OutputResult()
        # # self.RxD('t 0\r')
        # # self.RxD('g r0x24\r')
    # 反馈
        # self.RxD('enc clear\r')
        # a0 = self.RxD('g r0xa0\r') # Event Status Register(0xA0). Bits: 0~31
        # a1 = self.RxD('g r0xa1\r')
        # a4 = self.RxD('g r0xa4\r')
        # self.RxD('s r0xa4 512\r')
        # print('A0: {}\nA1: {}\nA4: {}'.format(BitsMapped_ES('0xA0', a0[2:]), BitsMapped_ES('0xA0', a1[2:]), BitsMapped_ES('0xA4', a4[2:])))
        # self.RxD('s r0xa1 {}\r'.format(a1[2:]))

        # self.RxD('g r0xcb\r') # Trajectory Maximum Velocity. Units: 0.1 counts/s.
        # self.RxD('g r0xcc\r') # Maximum acceleration rate(0xcc). Units: 10 counts/second2.
        # self.RxD('g r0x20\r') # Drive Temperature A/D Reading. Units: degrees C.
        # self.RxD('g r0x38 \r') # Actual Motor Current. Units: 0.01 A.
        # self.RxD('g r0x1E\r') # High Voltage A/D Reading. Units: 100 mV.

        # self.RxD('g r0x3d \r') # Trajectory Destination Position. Units: encoder counts.
    # Encoder
        # self.RxD('g r0x32\r') # Motor position. Units: counts. 
        # self.RxD('s r0x32 0\r') # Motor position. Units: counts.
        # self.RxD('g r0x2d \r') # R*_Commanded Position. Units: counts. / 位置模式下设置编码器的位置
        # self.RxD('g r0x17\r') # Motor position. Units: counts. For single feedback systems, this value is same as Actual Motor Position (0x32).
        # self.RxD('s r0x17 0\r') # 设置编码器的实际位置，区别于0x2d
    # 归位
        # self.RxD('g r0xc6\r') # Home Offset(0xc6_RF). Units: counts. 
        # self.RxD('g r0xc2 \r') # Homing Method Configuration. Bits: 0~15

        # self.RxD('s r0x24 21\r') # Desired State(0x24). Bits: 0~42(P19)
        # self.RxD('s r0xc2 \r') # Homing Method Configuration. Bits: 0~15
        # self.RxD('s r0xc3 \r') # Homing Velocity (fast moves)(0xc3). Units: 0.1 counts/s.
        # self.RxD('s r0xc4 \r') # Homing Velocity (slow moves)(0xc4). Units: 0.1 counts/s.
        # self.RxD('s r0xc5 \r') # Homing Acceleration/Deceleration(0xc5). Units: 10 counts/s2.
        # self.RxD('s r0xc6 \r') # Home Offset(0xc6). Units: counts. 
        # self.RxD('s r0xc7 \r') # Homing Current Limit(0xc7). Units: 0.01 A.

        # self.RxD('s r0xbf \r') # Home to Hard Stop Delay Time. Units: ms.

        # self.RxD('s r0xb8 352256\r') # Positive Software Limit value(0xb8). Units: counts.
        # self.RxD('s r0xb9 352256\r') # Negative Software Limit(0xb9). Units: counts. 
        # self.RxD('t 1\r')
    # Baud
        # self.RxD('g r0x90\r') # Serial Port Baud Rate. Units: bits/s.
        # self.RxD('g r0xc1\r') # CAN Network Node ID Configuration./# 50,000 = 0101 0000 0000 0000
        # self.OutputResult()

# %%
def main():
    ports = Port() # 创建Port()类
    ports.Write() # 写入ASCII

# Program start from here
if __name__ == '__main__':
    main()