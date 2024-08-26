#! /usr/bin/env python
# -*- coding:utf-8 -*-

# %% import
# Lib
# import smbus
import smbus2 as smbus
import time
# Constant
from imu_lib.Constant_JY901b import *

# %% Class
class JY901B(object):
    '''
    '''
    def __init__(self):
        self.addr = DEFAULT_ADDRESS
        self.i2c = smbus.SMBus(1)
# ==================================================
#                                             Device Info
# ==================================================
    def device_return_rate(parameter_list):
        """
            RSW = 0x02 # 回传数据内容
            RATE = 0x03 # 回传数据速率
            BAUD = 0x04 # 串口波特率
        """
        pass
    def device_temp(self):
        """
            TEMP = 0x40 # 模块温度
        
            温度计算公式：
            T=((TH<<8)|TL) /100 ℃
        """
        try:
            raw_temp = self.i2c.read_i2c_block_data(self.addr, TEMP, 2)
        except IOError:
            print('ReadError: temp_raw')
            return 0
        else:
            temp = (raw_temp[1] << 8 | raw_temp[0]) / 100.0 # ℃
        return temp
# ==================================================
#                                            Get Pressure & Height
# ==================================================
    def get_pressure(self):
        """
            PRESSUREL = 0x45 # 气压低字
            PRESSUREH = 0x46 # 气压高字

            0x55 0x56 P0 P1 P2 P3 H0 H1 H2 H3 SUM
            气压P = ( P3<<24)| ( P2<<16)| ( P1<<8)| P0 （Pa）
        """
        try:
            raw_pressure_l = self.i2c.read_i2c_block_data(self.addr, PRESSUREL, 2)
            raw_pressure_h = self.i2c.read_i2c_block_data(self.addr, PRESSUREH, 2)
        except IOError:
            print('ReadError: pressure_raw')
            return 0
        else:
            pressure = (raw_pressure_h[1]<<24 | raw_pressure_h[0]<<16 | raw_pressure_l[1]<<8 | raw_pressure_l[0])
        return pressure
    def get_height(self):
        """
            HEIGHTL = 0x47 # 高度低字
            HEIGHTH = 0x48 # 高度高字

            0x55 0x56 P0 P1 P2 P3 H0 H1 H2 H3 SUM
            高度H = ( H3<<24)| ( H2<<16)| ( H1<<8)| H0 （cm）

            将单位转换为: m
        """
        try:
            raw_height_l = self.i2c.read_i2c_block_data(self.addr, HEIGHTL, 2)
            raw_height_h = self.i2c.read_i2c_block_data(self.addr, HEIGHTH, 2)
        except IOError:
            print('ReadError: height_raw')
            return 0
        else:
            height = (raw_height_h[1]<<24 | raw_height_h[0]<<16 | raw_height_l[1]<<8 | raw_height_l[0])
            height = height/100 # unit: m
        return height
# ==================================================
#                                             Get Position
# HX = 0x3a # X 轴磁场
# HY = 0x3b # Y 轴磁场
# HZ = 0x3c # Z 轴磁场
# Q0 = 0x51 # 四元素Q0
# Q1 = 0x52 # 四元素Q1
# Q2 = 0x53 # 四元素Q2
# Q3 = 0x54 # 四元素Q3
# ==================================================
    def get_accel_data(self):
        '''
            AX = 0x34 # X 轴加速度
            AY = 0x35 # Y 轴加速度
            AZ = 0x36 # Z 轴加速度
        '''
        try:
            self.raw_acc_x = self.i2c.read_i2c_block_data(self.addr, AX, 2)
            self.raw_acc_y = self.i2c.read_i2c_block_data(self.addr, AY, 2)
            self.raw_acc_z = self.i2c.read_i2c_block_data(self.addr, AZ, 2)
        except IOError:
            print('ReadError: gyro_acc')
            return (0, 0, 0)
        else:
            self.k_acc = 16
            self.acc_x = (self.raw_acc_x[1] << 8 | self.raw_acc_x[0]) / 32768.0 * self.k_acc
            self.acc_y = (self.raw_acc_y[1] << 8 | self.raw_acc_y[0]) / 32768.0 * self.k_acc
            self.acc_z = (self.raw_acc_z[1] << 8 | self.raw_acc_z[0]) / 32768.0 * self.k_acc
            if self.acc_x >= self.k_acc:
                self.acc_x -= 2 * self.k_acc
            if self.acc_y >= self.k_acc:
                self.acc_y -= 2 * self.k_acc
            if self.acc_z >= self.k_acc:
                self.acc_z -= 2 * self.k_acc
        return {'x': self.acc_x, 'y': self.acc_y, 'z': self.acc_z}
    def get_gyro_data(self):
        '''
            GX = 0x37 # X 轴角速度
            GY = 0x38 # Y 轴角速度
            GZ = 0x39 # Z 轴角速度
        '''
        try:
            self.raw_gyro_x = self.i2c.read_i2c_block_data(self.addr, GX, 2)
            self.raw_gyro_y = self.i2c.read_i2c_block_data(self.addr, GY, 2)
            self.raw_gyro_z = self.i2c.read_i2c_block_data(self.addr, GZ, 2)
        except IOError:
            print('ReadError: gyro_gyro')
            return (0, 0, 0)
        else:
            self.k_gyro = 2000
            self.gyro_x = (self.raw_gyro_x[1] << 8 | self.raw_gyro_x[0]) / 32768.0 * self.k_gyro
            self.gyro_y = (self.raw_gyro_y[1] << 8 | self.raw_gyro_y[0]) / 32768.0 * self.k_gyro
            self.gyro_z = (self.raw_gyro_z[1] << 8 | self.raw_gyro_z[0]) / 32768.0 * self.k_gyro
            if self.gyro_x >= self.k_gyro:
                self.gyro_x -= 2 * self.k_gyro
            if self.gyro_y >= self.k_gyro:
                self.gyro_y -= 2 * self.k_gyro
            if self.gyro_z >= self.k_gyro:
                self.gyro_z -= 2 * self.k_gyro
        return {'x': self.gyro_x, 'y': self.gyro_y, 'z': self.gyro_z}
    def get_angle(self):
        '''
            ROLL_X = 0x3d # 轴角度
            PITCH_Y = 0x3e # 轴角度
            YAW_Z = 0x3f # 轴角度
        '''
        try:
            self.raw_angle_x = self.i2c.read_i2c_block_data(self.addr, ROLL_X, 2)
            self.raw_angle_y = self.i2c.read_i2c_block_data(self.addr, PITCH_Y, 2)
            self.raw_angle_z = self.i2c.read_i2c_block_data(self.addr, YAW_Z, 2)
            # print('{}{}{}'.format(self.raw_acc_x, self.raw_acc_y, self.raw_acc_z))
        except IOError:
            print('ReadError: gyro_angle')
            return {'x': 0, 'y': 0, 'z': 0}
        else:
            self.k_angle = 180
            self.angle_x = (self.raw_angle_x[1] << 8 | self.raw_angle_x[0]) / 32768.0 * self.k_angle
            self.angle_y = (self.raw_angle_y[1] << 8 | self.raw_angle_y[0]) / 32768.0 * self.k_angle
            self.angle_z = (self.raw_angle_z[1] << 8 | self.raw_angle_z[0]) / 32768.0 * self.k_angle
            if self.angle_x >= self.k_angle:
                self.angle_x -= 2 * self.k_angle
            if self.angle_y >= self.k_angle:
                self.angle_y -= 2 * self.k_angle
            if self.angle_z >= self.k_angle:
                self.angle_z -= 2 * self.k_angle
        return {'x': self.angle_x, 'y': self.angle_y, 'z': self.angle_z}

def main():
    jy901b = JY901B()
    while(True):
        print(' Acc: ' + repr(jy901b.get_accel_data()))
        print('Gyro: ' + repr(jy901b.get_gyro_data()))
        print('Angle:' + repr(jy901b.get_angle()))
        print('Temp: {}'.format( jy901b.device_temp()))
        print('Pressure: {}'.format( jy901b.get_pressure()))
        print('Height: {}'.format( jy901b.get_height()))
        print('--- --- ---')
        time.sleep(0.5)

if __name__ == '__main__':
    main()