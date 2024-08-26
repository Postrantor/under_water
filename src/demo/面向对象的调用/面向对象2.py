#! /usr/bin/env python
# -*- coding:utf-8 -*-

class classname1(object):
    """
    docstring
    """

    def __init__(self, arg1):
        self.arg = arg1
        print(self.arg)

    def fun1(self, name):
        print('class1.fun1{}'.format(name))

    def fun1_1(self):
        if self.arg1 == 1:
            print('a"r"g1: {}'.format(self.arg1))


class classname2(object):
    """
    docstring
    """

    def fun2(self, name):
        print('class2.fun2{}'.format(name))


class classname3(classname1, classname2):
    """
    docstring
    """
    # def __init__(self,arg3):
    #     classname1.__init__(self,arg3)

    def __init__(self, arg1):
        super(classname3, self).__init__(arg1)

    def fun3(self, name1, name2):
        self.arg1 = 1
        self.arg = 'arg3'
        print(self.arg)
        print(classname1.fun1_1(self))
        print(classname1.fun1(self, name=name1))
        print(classname2.fun2(self, name=name2))

# class_test = classname3()
# class_test.fun3(name1='name11', name2='name12')


# class_test1 = classname1('arg1')
class_test2 = classname3('arg1')
class_test2.fun3('name1', 'name2')
