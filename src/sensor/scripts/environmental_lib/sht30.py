# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''md
    Distributed with a free-will license.
    Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
    This code is designed to work with the SHT30_I2CS I2C Mini Module available from ControlEverything.com.
    https://www.controleverything.com/content/Humidity?sku=SHT30_I2CS#tabs-0-product_tabset-2
    https://github.com/costastf/temperature_sensor_mqtt
'''
__version__ = '0.0.1'
__author__ = 'Postrantor'
__license__ = "Apache License 2.0. https://www.apache.org/licenses/LICENSE-2.0"

# %% import
# Lib
# import smbus
import smbus2 as smbus
import time

# %% Constant
# I2C address of the device
SHT30_DEFAULT_ADDRESS = 0x44
# SHT30 Command Set
SHT30_MEAS_REP_STRETCH_EN = 0x2C  # Clock stretching enabled
SHT30_MEAS_HIGH_REP_STRETCH_EN = 0x06  # High repeatability measurement with clock stretching enabled
SHT30_MEAS_MED_REP_STRETCH_EN = 0x0D  # Medium repeatability measurement with clock stretching enabled
SHT30_MEAS_LOW_REP_STRETCH_EN = 0x10  # Low repeatability measurement with clock stretching enabled
SHT30_MEAS_REP_STRETCH_DS = 0x24  # Clock stretching disabled
SHT30_MEAS_HIGH_REP_STRETCH_DS = 0x00  # High repeatability measurement with clock stretching disabled
SHT30_MEAS_MED_REP_STRETCH_DS = 0x0B  # Medium repeatability measurement with clock stretching disabled
SHT30_MEAS_LOW_REP_STRETCH_DS = 0x16  # Low repeatability measurement with clock stretching disabled
SHT30_CMD_READSTATUS = 0xF32D  # Command to read out the status register
SHT30_CMD_CLEARSTATUS = 0x3041  # Command to clear the status register
SHT30_CMD_SOFTRESET = 0x30A2  # Soft reset command
SHT30_CMD_HEATERENABLE = 0x306D  # Heater enable command
SHT30_CMD_HEATERDISABLE = 0x3066  # Heater disable command

# %% Class


class SHT30():
    def __init__(self):
        self.bus = smbus.SMBus(1)  # get I2C bus
        self.write_command()
        time.sleep(0.3)
        self.read_data()

    def write_command(self):
        '''Select the temperature & humidity command from the given provided values'''
        COMMAND = [SHT30_MEAS_HIGH_REP_STRETCH_EN]
        self.bus.write_i2c_block_data(SHT30_DEFAULT_ADDRESS, SHT30_MEAS_REP_STRETCH_EN, COMMAND)

    def read_data(self):
        '''Read data back from device address, 6 bytes
        temp MSB, temp LSB, temp CRC, humidity MSB, humidity LSB, humidity CRC'''
        # [issue]:
        # smbus和smbus2的区别，需要指定一下起始的寄存器地址：0x00
        # smbus也可以这样写，这个参数应该是默认的，没有核实
        data = self.bus.read_i2c_block_data(SHT30_DEFAULT_ADDRESS, 0x00, 6)
        # Convert the data
        temp = data[0] * 256 + data[1]
        temp_C = -45 + (175 * temp / 65535.0)
        temp_F = -49 + (315 * temp / 65535.0)
        humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
        return {'temp_C': temp_C, 'temp_F': temp_F, 'hum': humidity}

    def update(self):
        # [issue]:
        # 不能一直读取吗？
        self.write_command()
        time.sleep(0.3)
        result = self.read_data()
        return result

    def update_test(self):
        while True:
            self.write_command()
            # time.sleep(0.3)
            result = self.read_data()
            print('Relative Humidity : %.2f %%' % (result['hum']))
            print('Temperature in Celsius : %.2f °C' % (result['temp_C']))
            print(' --- --- ---')
            time.sleep(0.1)

# %%


def main():
    sht30 = SHT30()
    sht30.update_test()
    # sht30.update()


if __name__ == '__main__':
    main()
