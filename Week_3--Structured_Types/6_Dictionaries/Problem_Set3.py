# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:41:02 2021

@author: SRI
"""

'''
Problem 3
10.0/10.0 points (graded)
Implement a function called closest_power that meets the specifications below.

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
For example,

closest_power(3,12) returns 2
closest_power(4,12) returns 2
closest_power(4,1) returns 0




def closest_power(base, num):
    
    #define spare variables
    exp = 0
    check = 0
    #convert to int
    num = int(num)

    while exp < num:
        check = base ** exp
        beforeInc = num - base ** exp
        afterInc = num - base ** (exp + 1)
        if abs(afterInc) >= beforeInc:
            return exp