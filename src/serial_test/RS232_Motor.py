#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''
    这个就是作为一个库，主要是针对电机
    这里会调用驱动的函数，被主函数调用，就像接线一样
'''

# %% import
# Lib
import os
# Hardware
import motor_lib.Motor as Motor

# %% Constant
# Serial
from constant_lib.Constant_Serial import *

# %% main


def main():
    Motor_UCR_L = Motor.MotorClass(PortID=PortID_UCR, NodeID=0, Mode='Speed',
                                   vel=0, acc=1000000, dec=1000000)
    argout = Motor_UCR_L.dev_status()
    print(argout)


if __name__ == '__main__':
    main()
