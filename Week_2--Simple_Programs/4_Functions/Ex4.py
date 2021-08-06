# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 17:41:30 2021

@author: SRI
"""
a = 10
def f(x):
      return x + a
a = 3
print(f(1))



x =12
def g(x):
    x = x+1
    print(x)
    def h(y):
        return x+y
    return h(6)



print(g(x))



