#! /usr/bin/env python
# -*- coding:utf-8 -*-

'''
切割字符串
# https://www.jb51.net/article/119202.htm
'''

a = '0103180001000002041e6000001001000000030009000000000000f92b'
print(''.join([str(int(b, 16))+'-' for b in [a[i:i+4] for i in range(6, len(a), 4)]]))
# 从第六个开始读取，步长为4；从第一个开始取，步长为4；将字符串按16进制转换成整数(10进制)；合并为元组；


al = []
for i in range(6, len(a), 4):
    b = a[i:i+4]
    al.append(str(int(b, 16)))
print(al[3])
