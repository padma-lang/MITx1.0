# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 17:26:28 2021

@author: SRI
"""

def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)


print(a(False, 2, 3))

print(b(3, 2))

print(a(3>2, a, b))


def a(x,y,z):
    return a

print(3>2,4,5)
"""

print(b(a, b))

"""
