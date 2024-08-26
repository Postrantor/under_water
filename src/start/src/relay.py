#! /usr/bin/python
# -*- coding:UTF-8 -*-

'''
'''

# %%
# Lib
import RPi.GPIO as RPi_GPIO

# %%
# defain引脚常量
Enable = 5
# set GPIO引脚编号规则
RPi_GPIO.setmode(RPi_GPIO.BCM)
# set GPIO引脚的输入(RPi_GPIO.IN)/输出(RPi_GPIO.OUT)/默认值(initial=RPi_GPIO.HIGH)
# RPi_GPIO.setup(Enable, RPi_GPIO.OUT, initial=RPi_GPIO.HIGH)
RPi_GPIO.setup(Enable, RPi_GPIO.OUT, initial=RPi_GPIO.LOW)

print(Enable)