#! /usr/bin/env python
# -*- coding:utf-8 -*-
import os


def mk_dir(path):
    path = path.strip()  # 去除首位空格
    path = path.rstrip("\\")  # 去除尾部 \ 符号
    isExists = os.path.exists(path)  # 判断路径是否存在
    if not isExists:  # 如果不存在则创建目录
        os.makedirs(path)  # 创建目录操作函数
        print(path + ' Successful')
        return path
    else:  # 如果目录存在则不创建，并提示目录已存在
        print(path + ' Exist')
        return path
