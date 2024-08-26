#! /usr/bin/env python
# -*- coding:utf-8 -*-

# %%
from copley.scripts.copley_lib.ParamDict_HomingMethod import BitsMapped as BitsMapped_HM
from copley.scripts.copley_lib.ParamDict_EventStatus import BitsMapped as BitsMapped_ES

class classname1(object):
    def class1_fun1(self):
        self.name = 'class1_fun1'
        print('classname1 have {}'.format(self.name))
# # from demo.OOP_1_1 import classname1_1
# class classname2(classname1,classname1_1):
#     def class2_fun1(self):
#         self.name = 'class2_fun1'
#         print('classname2 have {}'.format(self.name))
#     def class2_fun2(self):
#         self.name = 'class2_fun2'
#         print('classname2 have {}'.format(self.name))
#         self.class1_fun1()
#         print('classname2 have {}'.format(self.name)) # 也就是说，这个变量是可以改变的
#         self.class1_1_fun1()
#         print('classname2 have {}'.format(self.name)) # 也就是说，这个变量是可以改变的

# class2 = classname2()
# class2.class2_fun2()

# %%
from demo.OOP_1_1 import *
class classname3(classname1,classname1_1):
    """
    docstring
    """
    def class3_fun1(self):
        print('classname3')
    def class3_fun2(self):
        self.class1_fun1()
        # arg1 = BitsMapped_ES('0xA0',0)
        arg1 = BitsMapped_HM('0xC2','532')
        print('{}\n'.format(arg1))

class3 = classname3()
class3.class1_1_fun1()
# class3.class3_fun2()
# arg = class2.EventStatus_0xA0(4)
# print(arg)

# %% 导入常量
# import demo.demo3 as unit
# print(unit.unit_1)
# print(unit.unit_2)
# print(unit.unit_3)

# from demo.demo3 import *
# print(unit_1)
# print(unit_2)
# print(unit_3)