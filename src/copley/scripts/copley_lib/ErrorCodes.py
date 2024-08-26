#! /usr/bin/env python
# -*- coding:utf-8 -*-

# %% doc
__all__ = ['CodesMapped']  # 可用于模块导入时限制，只有__all__内指定的属性、方法、类可被导入
__docformat__ = 'restructuredtext'  # 允许诸如 epydoc之类的python文档生成器工具知道如何正确解析模块文档

# %%


class ErroeCodes(object):
    """
    """

    def __init__(self):
        # self.ascii = ascii
        # self.data = data
        pass

    def __str__(self):
        msg = 'from copley.scripts.copley_lib.ErrorCodes import CodesMapped'
        return msg


def CodesMapped(error='e', code=0):
    argout = ''
    if error == 'e':
        argout = CodeMapped(int(code))
    return argout


def CodeMapped(idx):
    '''
        Code    Meaning
        1   Too much data passed with command
        3   Unknown command code
        4   Not enough data was supplied with the command
        5   Too much data was supplied with the command
        9   Unknown parameter ID
        10  Data value out of range
        11  Attempt to modify read-only parameter
        14  Unknown axis state
        15  Parameter doesn’t exist on requested page
        16  Illegal serial port forwarding
        18  Illegal attempt to start a move while currently moving
        19  Illegal velocity limit for move
        20  Illegal acceleration limit for move
        21  Illegal deceleration limit for move
        22  Illegal jerk limit for move
        25  Invalid trajectory mode
        27  Command is not allowed while CVM is running
        31  Invalid node ID for serial port forwarding
        32  CAN Network communications failure
        33  ASCII command parsing error
        36  Bad axis letter specified
        46  Error sending command to encoder
        48  Unable to calculate filter
    '''
    if idx == 0:
        argout = 'Code_00: Too much data passed with command\n'
    elif idx == 1:
        argout = 'Code_03: Unknown command code\n'
    elif idx == 2:
        argout = 'Code_04: Not enough data was supplied with the command\n'
    elif idx == 3:
        argout = 'Code_05: Too much data was supplied with the command\n'
    elif idx == 4:
        argout = 'Code_09: Unknown parameter ID\n'
    elif idx == 5:
        argout = 'Code_10: Data value out of range\n'
    elif idx == 6:
        argout = 'Code_11: Attempt to modify read-only parameter\n'
    elif idx == 7:
        argout = 'Code_14: Unknown axis state\n'
    elif idx == 8:
        argout = 'Code_15: Parameter doesn’t exist on requested page\n'
    elif idx == 9:
        argout = 'Code_16: lllegal serial port forwarding\n'
    elif idx == 10:
        argout = 'Code_18: Illegal attempt to start a move while currently moving\n'
    elif idx == 11:
        argout = 'Code_19: Illegal velocity limit for move\n'
    elif idx == 12:
        argout = 'Code_20: Illegal acceleration limit for move\n'
    elif idx == 13:
        argout = 'Code_21: Illegal deceleration limit for move\n'
    elif idx == 14:
        argout = 'Code_22: Illegal jerk limit for move\n'
    elif idx == 15:
        argout = 'Code_25: Invalid trajectory mode\n'
    elif idx == 16:
        argout = 'Code_27: Command is not allowed while CVM is running\n'
    elif idx == 17:
        argout = 'Code_31: Invalid node ID for serial port forwarding\n'
    elif idx == 18:
        argout = 'Code_32: CAN Network communications failure\n'
    elif idx == 19:
        argout = 'Code_33: ASCII command parsing error\n'
    elif idx == 20:
        argout = 'Code_36: Bad axis letter specified\n'
    elif idx == 19:
        argout = 'Code_46: Error sending command to encoder\n'
    elif idx == 20:
        argout = 'Code_48: Unable to calculate filter\n'
    return idx, argout
