#! /usr/bin/env python
# -*- coding:utf-8 -*-

class demo():
    def fun(a, b, *args, **kwargs):
        """可变参数演示示例"""
        print("a =", a)
        print("b =", b)
        print("args =", args)
        print("kwargs: ", kwargs)
        # for key, value in kwargs.items():
        #     print(key, "=", value)

    def fun1(self):
        self.fun(1, 2, 3, 4, 5, m=6, n=7, p=8)  # 注意传递的参数对应
        # a = 1
        # b = 2
        # args = (3, 4, 5)
        # kwargs: 
        # p = 8
        # m = 6
        # n = 7

    # c = (3, 4, 5)
    # d = {"m":6, "n":7, "p":8}
    # fun(1, 2, *c, **d)    # 注意元组与字典的传参方式
    # a = 1
    # b = 2
    # args = (3, 4, 5)
    # kwargs: 
    # p = 8
    # m = 6
    # n = 7

    # fun(1, 2, c, d) # 注意不加星号与上面的区别
    # a = 1
    # b = 2
    # args = ((3, 4, 5), {'p': 8, 'm': 6, 'n': 7})
    # kwargs:

if __name__ == '__main__':
    demo1 = demo()
    demo1.fun1()
