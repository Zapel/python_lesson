#! /usr/bin/env python
# -*- coding: utf-8 -*-

def invert_array(A, N):
    """Invert Array"""
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]
    pass

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print (A1)
    invert_array(A1, 5)
    print (A1)

    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

test_invert_array()

def array_shift_left(A, N):
    tmp = A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp

def test_left_shift_array():
    A1 = [0, 1, 2, 3, 4]
    print (A1)
    array_shift_left(A1, 5)
    print (A1)

    if A1 == [1, 2, 3, 4, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

test_left_shift_array()

def array_shift_right(A, N):
    tmp = A[N-1]
    for k in range(N-2, -1, -1):
        A[k+1] = A[k]
    A[0] = tmp

def test_right_shift_array():
    A1 = [0, 1, 2, 3, 4]
    print (A1)
    array_shift_right(A1, 5)
    print (A1)

    if A1 == [4, 0, 1, 2, 3]:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

test_right_shift_array()