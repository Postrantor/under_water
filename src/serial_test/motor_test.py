#! /usr/bin/env python
# -*- coding:utf-8 -*-
'''README:
[20220419]:

[README]:
    这个就是作为一个库，主要是针对电机
    这里会调用驱动的函数，被主函数调用，就像接线一样
'''

# %% import
# Lib
import os
# Hardware
import motor_lib.Motor as Motor
# Constant
from constant_lib.Constant_Serial import *
from constant_lib.Constant_Motor import Maxon_266761, Maxon_305474, Maxon_306090


# %% main
def main():
    Motor_UCR = Motor.MotorClass(
        PortID=PortID_UCR,  # PortID_Wing, 
        NodeID=0,  # both 0 and 1
        Mode='Speed',  # Position, Speed, Current
        profile=0,
        pos=0,
        vel=Maxon_305474.Max_Vel,
        acc=500000,
        dec=500000)

    print(Motor_UCR.dev_status())
    # Motor_UCR.clearFaultRegister()

    # Motor_UCR.write_Position(1024*4*86*0, 1)
    # Motor_UCR.Move(1)

    Motor_UCR.write_Velocity(Maxon_306090.Max_Vel, 0)
    Motor_UCR.write_Velocity(Maxon_306090.Max_Vel/4, 1)


if __name__ == '__main__':
    main()
