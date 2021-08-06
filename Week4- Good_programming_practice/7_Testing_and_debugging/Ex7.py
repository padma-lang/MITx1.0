# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 00:04:36 2021

@author: SRI
"""

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)
  

print(f(3))