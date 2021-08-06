# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 23:39:05 2021

@author: SRI


"""

""" iter gcd"""

def gcdIter(a, b):
    
    c = min(a,b)
    
    while c >0:
        if (a%c)==0 and (b%c)==0:
            return c
        else:
            c -= 1
        
print(gcdIter(2,12))

""" gcd recur"""

def gcdRec(a,b):
    
    if b==0:
        return a
    else:
        
        return gcdRec(b, a%b)

print(gcdRec(2,12))
    
    
    

    
  




        
        
    