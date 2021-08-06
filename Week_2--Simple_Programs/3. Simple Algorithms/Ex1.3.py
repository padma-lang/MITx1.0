# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:53:10 2021

@author: SRI
"""

iteration =0
while iteration<5:
    count =0
    for letter in 'Hello!,world':
        count+=1
        if iteration%2==0:
            break
    print(f'Iteration: {iteration}, Count is: {count}')
    iteration+=1