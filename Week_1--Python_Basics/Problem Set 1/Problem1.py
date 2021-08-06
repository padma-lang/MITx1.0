# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 13:39:02 2021

@author: SRI

Problem 1
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s.
 Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
 For example, if s = 'azcbobobegghakl', your program should print:
     Number of vowels: 5
"""
s = input('Enter the string: ')
vowels = ['a','e','i','o','u']
count =0

for letter in s:
    if letter in vowels:
        count+=1
print(f'Number of vowels: {count}')
        