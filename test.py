# -*- coding: utf-8 -*-
__author__ = 'buzz'
__date__ = '2018/4/7 上午11:30'

import threading

a = 0


def test():
    threading.Timer(2.0, test).start()
    global a
    if a == 0:
        print("aaa")
        a = 1
    elif a == 1:
        print("bbb")
        a = 2
    else:
        print("ccc")
        a = 0


test()
