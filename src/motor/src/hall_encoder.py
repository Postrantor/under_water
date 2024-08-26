#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
这个只是将两个函数合并为一个Class，但是并为做测试
除此之外，与之相关的函数调用关系也并没调试，不过应该没关系
这个函数应该能集成到其他函数里面

模块的导入还要研究一下
'''

import motor.src.HallEncoderClass as Hall

def Left():
    counter_encoder = Hall.HallEncoderCounter()
    counter_encoder.initial_Pin(12, 13) # Left
    counter_encoder.initial_node('lwheel_enc') # 声明Publisher
    counter_encoder.update()

def Right():
    counter_encoder = Hall.HallEncoderCounter()
    counter_encoder.initial_Pin(16, 17) # Left
    counter_encoder.initial_node('rwheel_enc') # 声明Publisher
    counter_encoder.update()


def main():
    Left()
    Right()

# Program start from here
if __name__ == '__main__':
    main()