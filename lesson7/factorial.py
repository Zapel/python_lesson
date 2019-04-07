# -*- coding: utf-8 -*-

from __future__ import print_function



def f(n):
    input(n)
    assert n>=0, "Факториал отрицательного не определен"
    if n == 0:
        return 1
    return f(n-1)*n

