# -*- coding: utf-8 -*-

from __future__ import print_function

def matryoshka(n):
    if n == 1:
        print("Матрешечка")
    else:
        print("Верх матрешки n=", n)
        matryoshka(n-1)
        print("Низ матрешки n=", n)


matryoshka(5)