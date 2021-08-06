# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 21:21:21 2021

@author: SRI
"""

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return a*(x**2)+b*(x)+c

print(evalQuadratic(3,5,1,2))