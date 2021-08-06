# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 07:19:41 2021

@author: SRI
"""

def fib(a):
    
    if a== 0 or a == 1:
        return 1
    else:
        return fib(a-1) + fib(a-2)
        

print(fib(5))