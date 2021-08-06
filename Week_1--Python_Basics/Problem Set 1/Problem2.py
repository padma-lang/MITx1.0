# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 13:44:14 2021

@author: SRI


Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
 For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
count=0

s = input('enter the word: ')

for i,_ in enumerate(s):
    if s[i:i+3]=='bob':
        count+=1
        print(count)
print(f'Number of times bob occurs is: {count}')
    
    