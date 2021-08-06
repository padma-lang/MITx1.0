# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 06:20:24 2021

@author: SRI
"""

number = 125
guess =0
epsilon =0.01
increment = 0.001
iteration =0

while abs(guess**3-number)>= epsilon and guess<number:
    guess+=increment
    iteration+=1
print(f'The number of iterations it took: {iteration}')
if abs(guess**3-number) >=epsilon:
    print(f'The cube root is cube failed at: {guess}')
    
else:
    print(f' {guess} is the closest cube root of : {number}')
    

    
    
    