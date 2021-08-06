# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:00:41 2021

@author: SRI
"""

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

print(applyEachTo([inc, square, halve, abs], -3))
print(applyEachTo([inc, square, halve, abs], 3.0))
print(applyEachTo([inc], -3))