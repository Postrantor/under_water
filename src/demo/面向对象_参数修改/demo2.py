#! /usr/bin/env python
# -*- coding:utf-8 -*-
from demo.demo_20210319.demo1 import demo1


class demo2(demo1):
    """
    docstring
    """

    def apply_pid(self):
        # self.Kp = 5
        self.update_pid()
