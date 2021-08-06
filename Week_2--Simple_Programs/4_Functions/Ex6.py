# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 18:33:02 2021

@author: SRI
"""

str1 = 'exterminate!' 
str2 = 'number one - the larch'

print(str1.upper)
print(str1.upper())
print(str1)
print(str1.isupper())
print(str1.islower())
str2 = str2.capitalize()
print(str2)
print(str1.index('e'))
print(str2.find('n'))

print(str2.find('!'))
print(str1.count('e'))
str1 = str1.replace('e', '*')
print(str1)
print(str2.swapcase())
print(str2.index('n'))
print(str2.replace('one', 'seven'))
print(str1.upper)
print(str2.replace('one', 'seven'))

'''
print(str2.index('!'))
'''