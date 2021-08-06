# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 08:18:23 2021

@author: SRI
"""

'guessing incremental algo'

x = 9
guess =0.0
counter =0
increment =0.01
epsilon =0.01

while abs(guess -x)>= epsilon:
    if guess <= x:
        guess+=increment
        counter+=1
    else:
        break
if abs(guess**2 -x) < epsilon:
        print(counter)
        print(f'succeeded: {guess}')
   
    
else:
     print('failed')

x =9
guess =0.0
epsilon =0.01
counter =0
increment =0.01

while guess<= x:
    if abs(guess**2 -x)< epsilon:
        break
    else:
        guess+=increment
        counter+=1
    
if abs(guess**2-x) >= epsilon:
    print('failed')
else:
    print(counter)
    print(f'succeeded: {guess}')
    
'Bisection search'

x =25
epsilon = 0.01
counter = 0
low = 0.0
high = x
guess = (high+low)/2.0

while abs(guess**2-x)>= epsilon:
    if guess**2<x:
        low = guess
        counter+=1
    else:
        high = guess
    guess = (high+low)/2.0

print(counter)
print(f'{guess} is close to the square root of {x}')

'Newton-Raphson'






        


 

