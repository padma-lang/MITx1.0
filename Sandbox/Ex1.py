# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 22:04:48 2021

@author: SRI
"""
s = 'azcbobobegghakl'
count = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print("Number of vowels:" + str(count))

