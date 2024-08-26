#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    [20210416]:
        有时候会崩溃，需要设置容错能力
        在关闭继电器的时候会断电，是因为我把供电接在了24伏上，需要更改
        直接从电源引出来供电，这样的话，电源就要多一个接头
        或者用5V供电，不知道可以吗，这个优先试试
    [20201130]:
        [Issue]: 还可以再补充一些内容
        1. 添加了基础的功能，获取全部的13个参数值，并进行分割、处理，主要是小数点以及进制的转换；
        2. 这里仅仅是读取地址值，应该还能执行写操作，这里暂时保留；对于写操作，还是先通过元件本身的按钮进行操作；
    [README]:
        库仑计的库函数：
        通讯接口：
            通讯接口：485(TTL_2_USB)
            通讯速率：115200
        参数设置：
            电池容量：
            电压：
            电流：
            功率：
            ...
        电压量程：0.0000---95.000V(过量程会有-OVLD-V 提示，10V 以内显示4 位小数，超过10V 自动切换为3 位小数)
        电流量程：±0.0000---9.9999A(过量程会有-OVLD-A 提示，10A 以内显示4 位小数)可以测量正负双向电流
        负载功率：0.0000---9999.9W(不同功率时小数位自动切换)
        输出容量：0000mAh---9999.99Ah(可切换成Wh 统计，容量可断电记忆，正负双向容量可抵消)
        供电电压：最新宽电压版本，蓝色接线柱位置支持DC：6~36V 供电，推荐9V 或12V 供电。
        温度测量：-55~125℃（要加温度芯片才能显示温度，未接温度芯片显示-00.1℃.
        负载电阻：0.0000---999.99R(小数位自动切换，超量程会有--OVLD-R 提示)
        运行时间：0:00:00---99:59:59(2016-05-05 修改计时100 小时一个循环)
        背光控制：可通过按中间切换键开关背景光状态（也可设置电流小于设定值自动关闭背景光）。
        信号输出：可设置电压上限下限、电流上限下限、温度上限下限，输出高低电平信号，方便接LED 或智能控制电路。
        预留接口：预留蓝牙模块位置、Wifi 模块位置、3 路DAC 数控输出（可选功能，要用的自己加相应配件）。
'''

# %% import
# Lib
import serial
import time

# %% Constant
# default serial parameter
defaultPortID = '/dev/UCR_Coulomb'
# defaultPortID = '/dev/ttyUSB4'
defaultBaud = 115200
defaultTimeout = .1

# %% class


class CoulombClass():
    '''
        defined coulomb class
    '''
# ==================================================
#                                                Initial
# ==================================================

    def __init__(self):
        self.inits_serial()
        self.inits_parameter()

    def inits_serial(self, baud=defaultBaud, serialPort=defaultPortID, timeout=defaultTimeout):
        '''
            initial serial port, incloud timeout, port, baudrate
        '''
        self.CoulombSerial = serial.Serial()
        self.CoulombSerial.timeout = timeout
        self.CoulombSerial.port = serialPort
        self.CoulombSerial.baudrate = baud
        self.CoulombSerial.open()

    def inits_parameter(self):
        '''
            initial parameter
        '''
        self.seam = []
        self.sign = []
# ==================================================
#                                                Callback
# ==================================================

    def get_result(self, cmd):
        '''
            # 获取相应命令的返回值，此处无法使用read_until，因为在结尾不是固定的字符；
            # 所以指定了timeout，当设置波特率为115200时，可以使用0.05s作为时间限制，再短就不行了；
            # https://blog.csdn.net/xuzhexing/article/details/91043579
            # https://blog.csdn.net/wowocpp/article/details/79498276
        '''
        self.CoulombSerial.write(cmd)
        # 将获取的编码结果以hex方式编码，并返回；
        result = self.CoulombSerial.read_until('\r').encode("hex")  # 注意区分encode、decode
        return result

    def voltage(self):
        '''
            # 0x0003  当前电压值50V以内3位小数，超过50V切换为2位小数`6E 4A`
            # 电压量程：0.0000---95.000V(过量程会有-OVLD-V 提示，10V 以内显示4 位小数，超过10V 自动切换为3 位小数)
        '''
        sign = self.sign[1]
        split = self.seam[3]

        if sign == '3':  # 3位小数
            voltage = int(split) / 1000.0
        elif sign == '2':  # 2位小数
            voltage = int(split) / 100.0
        else:  # 容错处理
            # [issue]:
            # 将变量设置为全局变量，保留上一次的数值
            # 若这次读取数值发生错误，则直接引用上次不为空的数值
            print('Error Voltage')
        return voltage

    def current(self):
        '''
            # 0x0004  当前电流值50A以内3位小数，超过50A切换为2位小数`00 01`
            # 电流量程：±0.0000---9.9999A(过量程会有-OVLD-A 提示，10A 以内显示4 位小数)可以测量正负双向电流
        '''
        current = self.seam[4]
        # 判断符号
        sign = self.sign[2]  # 符号位
        if sign == '1':  # 负数
            current = -int(current)
        elif sign == '0':  # 正数
            current = int(current)
        else:
            print('Error Current Sign')
        # 判断小数位置
        dot = self.sign[3]  # 小数位
        if dot == '4':  # 4位小数
            current = current / 10000.0
        elif dot == '3':  # 3位小数
            current = current / 1000.0
        elif dot == '2':  # 2位小数
            current = current / 100.0
        else:
            print('Error Current')
        return current

    def watt(self):
        '''
            # 0x0006  当前功率值，2位小数位`00 00`
            负载功率：0.0000---9999.9W(不同功率时小数位自动切换)
        '''
        watt = int(self.seam[6]) / 100.0

        return watt

    def resistance(self):
        '''
            这个没有地址位，直接是电压/电流=负载电阻
            # https://www.cnblogs.com/xiangnan/p/3419119.html
        '''
        voltage = self.voltage()
        current = self.current()
        if current == 0:
            resistance = float('inf')
        else:
            resistance = voltage / current

        return resistance

    def power(self):
        '''
            - 0x0007  当前剩余Ah电量，1位小数`00 03`
            - 0x0008  当前已耗Wh电能，无小数`00 08`
            - 0x0009  电池预设标称容量，1位小数`00 00`
            - 0x000B  剩余电量百分比，2位小数`00 00`
            输出容量：0000mAh---9999.99Ah(可切换成Wh 统计，容量可断电记忆，正负双向容量可抵消)
        '''
        remaining = int(self.seam[7]) / 10.0
        consumed = int(self.seam[8])
        capacity = int(self.seam[9]) / 10.0
        percentage = int(self.seam[11]) / 100.0
        return {'remaining': remaining, 'consumed': consumed, 'capacity': capacity, 'percentage': percentage}
# ==================================================
#                                                Split
# ==================================================

    def split(self):
        '''
            将获得的返回值从第6位起始，按步长4进行拆分，前6位不知道是啥；
            将获得的返回值中第[14, 18]的数值，按步长1进行拆分，判别电压、电流的正负以及小数位个数；
            - 0x0000  device id number`00 01`
            - 0x0001  当前设置界面步骤`00 00`
            - 0x0002  高位:副电压+主电压小数位；低位:电流正负及小数位`03 04`
        '''
        value = self.value_all  # 0x0000~0x000B
        for i in range(6, len(value), 4):  # Starting from the `6` position, split in steps of `4`
            block = str(int(value[i:i + 4], 16))
            self.seam.append(block)

        sign = value[14:18]  # 0x0002
        for j in range(0, len(sign), 1):  # Starting from the `0` position, split in steps of `1`
            block = str(int(sign[j:j + 1]))
            self.sign.append(block)
# ==================================================
#                                                Update
# ==================================================

    def update(self):
        '''
            调用RxD()函数，写入HEX；
            指令：前2个不知道是啥，后两个是起始地址位，后两个是读取的个数，后两个应该是校验位；
            结果：前3个不知道是啥，后两个是校验位
            # https://www.jb51.net/article/119202.htm
            # print ''.join([str(int(b, 16))+' ' for b in [result[i:i+4] for i in range(6, len(result[6:]), 4)]])
        '''
        address_all = [0x01, 0x03, 0x00, 0x00, 0x00, 0x0C, 0x45, 0xCF]  # 从第0个地址开始读取，连续读取12个地址位的数据
        self.value_all = self.get_result(address_all)
        # print(self.value_all)
        self.inits_parameter()  # 因为是对元组追加，所以每次运算前，需要清空
        self.split()
        # 0x0005  当前温度值首位为1时为负温，1位小数位`10 01`
        # 0x000A  电压超过设定值自动重置电量为满电状态，1位小数`00 00`

# %%


def main():
    coulomb = CoulombClass()
    coulomb.update()


# Program start from here
if __name__ == '__main__':
    main()

'''
10进制结果    所对应数值    16避制结果       数据地址位    数据备注项
00001           00001           0x00 0x01           0x0000          地址0000H本设备地址ID号
00000           00000           0x00 0x00           0x0001          地址0001H当前设置界面步骤
00787           00787           0x03 0x13          0x0002           地址:0002H高位:副电压+主电压小数位；低位:电流正负及小数位

00000           0. 000V           0x00 0x00       0x0003           地址:0003H当前电压值50V以内3位小数，超过50V切换为2位小数
00584           -0.584A           0x02 0x48       0x0004           地址:0004H当前电流值50A以内3位小数，超过50A切换为2位小数
04097           -0.1°C            0x10 0x01         0x0005           地址:0005H当前温度值首位为1时为负温，1位小数位
00000           0.00W           0x00 0x00         0x0006           地址:0006H当前功率值，2位小数位
00003           0.3Ah           0x00 0x03          0x0007           地址0007H当前剩余Ah电量，1位小数
00000           00000Wh       0x00 0x00       0x0008           地址0008H当前已耗Wh电能，无小数
00000           0.0Ah           0x00 0x00          0x0009           地址0009H电池预设标称容量，1位小数
00000           0.0V              0x00 0x00           0x000A            地址000AH电压超过设定值自动重置电量为满电状态，1位小数
00000           0.00%           0x00 0x00          0x000B           地址000BH剩余电量百分比，2位小数

# 单独读取一位
    cmd_00 = [0x01, 0x03, 0x00, 0x00, 0x00, 0x01, 0x84, 0x0A]
    self.RxD(cmd_00) # 仅读取电压位，即第0个地址位
    # 01 03 02 `00 01` 79 84 

    cmd_01 = [0x01, 0x03, 0x00, 0x01, 0x00, 0x01, 0xD5, 0xCA]
    self.RxD(cmd_01) # 仅读取电压位，即第1个地址位
    # 01 03 02 `00 00` B8 44 

    cmd_02 = [0x01, 0x03, 0x00, 0x02, 0x00, 0x01, 0x25, 0xCA]
    self.RxD(cmd_02) # 仅读取电压位，即第2个地址位
    # 01 03 02 `03 04` B9 77 

    cmd_03 = [0x01, 0x03, 0x00, 0x03, 0x00, 0x01, 0x74, 0x0A]
    self.RxD(cmd_03) # 仅读取电压位，即第3个地址位
    # 01 03 02 `6E 49` 55 D2 

    cmd_04 = [0x01, 0x03, 0x00, 0x04, 0x00, 0x01, 0xC5, 0xCB]
    self.RxD(cmd_04) # 仅读取电压位，即第4个地址位
    # 01 03 02 `00 01` 79 84 

    cmd_05 = [0x01, 0x03, 0x00, 0x05, 0x00, 0x01, 0x94, 0x0B]
    self.RxD(cmd_05) # 仅读取电压位，即第5个地址位
    # 01 03 02 `10 01` 74 44 

    cmd_06 = [0x01, 0x03, 0x00, 0x06, 0x00, 0x01, 0x64, 0x0B]
    self.RxD(cmd_06) # 仅读取电压位，即第6个地址位
    # 01 03 02 `00 00` B8 44 

    cmd_07 = [0x01, 0x03, 0x00, 0x07, 0x00, 0x01, 0x35, 0xCB]
    self.RxD(cmd_07) # 仅读取电压位，即第7个地址位
    # 01 03 02 `00 03` F8 45 

    cmd_08 = [0x01, 0x03, 0x00, 0x08, 0x00, 0x01, 0x05, 0xC8]
    self.RxD(cmd_08) # 仅读取电压位，即第8个地址位
    # 01 03 02 `00 08` B9 82 

    cmd_09 = [0x01, 0x03, 0x00, 0x09, 0x00, 0x01, 0x54, 0x08]
    self.RxD(cmd_09) # 仅读取电压位，即第9个地址位
    # 01 03 02 `00 00` B8 44 

    cmd_0A = [0x01, 0x03, 0x00, 0x0A, 0x00, 0x01, 0xA4, 0x08]
    self.RxD(cmd_0A) # 仅读取电压位，即第A个地址位
    # 01 03 02 `00 00` B8 44 

    cmd_0B = [0x01, 0x03, 0x00, 0x0B, 0x00, 0x01, 0xF5, 0xC8]
    self.RxD(cmd_0B) # 仅读取电压位，即第B个地址位
    # 01 03 02 `00 00` B8 44 
'''
