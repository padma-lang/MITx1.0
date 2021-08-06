# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 22:36:40 2021

@author: SRI
"""
s = 'azcbobobegghakl'
count = 0
for n in range(len(s)):
    if s[n:n+3] == "bob":
        count += 1

print("Number of times bob occurs is:" + str(count))