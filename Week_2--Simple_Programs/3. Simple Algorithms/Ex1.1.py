# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:03:52 2021

@author: SRI
"""

iteration =0
count =0
while iteration <5:
    for letter in "Hello!,world":
        count+=1
    print(f'Iteration : {iteration} ; count is: {count}')
    iteration+=1
    
        