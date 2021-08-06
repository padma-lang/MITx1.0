# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:24:35 2021

@author: SRI
"""

iteration =0

while iteration <5:
    count =0
    for letter in 'Hello!,world':
        count+=1
    print(f'Iteration: {iteration}, Count is: {count}')
    iteration+=1