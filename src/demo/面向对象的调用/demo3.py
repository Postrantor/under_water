#! /usr/bin/env python
# -*- coding:utf-8 -*-
from demo.OOP_1_1 import *
import time
class classname(object):
    """
    docstring
    """
    def demo1(self):
        file_thermal = "/sys/class/thermal/thermal_zone0/temp"
        try:
            while True:
                file = open(file_thermal)
                self.temp_actual = float(file.readline())/1000
                print("temp1 : %.2f" % self.temp_actual)
                time.sleep(0.5)
        except KeyboardInterrupt as e:
            file.close()
            print(e)

    def funcname(self):
        """
        docstring
        """
        cmd_max = 100
        cmd_min = 40
        temp_min = 35
        temp_max = 65
        slope = (cmd_max - cmd_min) / (temp_max - temp_min)
        intercept = cmd_max - slope * temp_max

        cmd = slope * self.temp_actual + intercept
        print("cmd : %.2f" % cmd)

# fan = classname()
# fan.demo1()
# fan.funcname()
# %%
# pwm_min = 40; pwm_max = 100
# temp_min = 0; temp_max = 65
# temp_actual = 60
# if temp_min < temp_actual < temp_max:
#     print(temp_actual)
# else:
#     print(100)

# %%
