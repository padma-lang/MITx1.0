# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 14:05:03 2021

@author: SRI


Problem 3
10.5/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s 
in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring.
 For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

count = 0
maxcount = 0
result = 0

s= input('enter the word: ')

for char in range(len(s) - 1):
    if (s[char] <= s[char + 1]):
        
        count += 1
        
        if count > maxcount:
            maxcount = count
            
            result = char + 1
            
           
    else:
        count = 0
startposition = result - maxcount
print('Longest substring in alphabetical order is:', s[startposition:result + 1])

