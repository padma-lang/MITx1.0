# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 17:06:55 2021

@author: SRI
"""

def applyToEach(L, f):
    l1 = []
    for i in range(len(L)):
        L[i] = f(L[i])
        a = L[i]
        l1.append(a)
    return l1
      
        
        
    

testList = [1, -4, 8, -9]

def int_num(a):
    return abs(a)

print(applyToEach(testList,int_num))


testList = [1, -4, 8, -9]

def adding(a):
    return a+1
    
print(applyToEach(testList,adding))


testList = [1, -4, 8, -9]
def twice(a):
    return a*a
    
print(applyToEach(testList,twice))



        




