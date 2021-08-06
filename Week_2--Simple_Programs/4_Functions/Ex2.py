# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 15:28:31 2021

@author: SRI
"""

def a(x):
   '''
   x: int or float.
   '''
   return x + 1

print(a(6))
print(a(a(a(6))))

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0

print(b(-5.3))

 
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y


print(c(a(1),b(1)))

'''
def d(x, y):
   
   x: Can be of any type.
   y: Can be of any type.
  
   return x > y

print(d('apple', 11.1))
'''
def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z
print(e(a(3), b(4), c(3, 4)))


def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2  
   
print(f)
