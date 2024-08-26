#! /usr/bin/env python
# -*- coding:utf-8 -*-
from demo.demo_20210319.demo2 import demo2


class demo3(demo2):
    """
    docstring
    """

    def func1(self):
        self.Kp = 10
        self.apply_pid()


demo = demo3()
demo.func1()
