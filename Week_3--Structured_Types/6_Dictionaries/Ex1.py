# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:23:40 2021

@author: SRI
"""

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

print(animals)
print(animals['c'])
#print(animals['donkey'])
print(len(animals))

animals['a'] = 'anteater'
print(animals['a'])
print(animals)
print(len(animals['a']))
print('baboon' in animals)
print('donkey' in animals.values())
print('b' in animals)
print(animals.keys())
del animals['b']
print(len(animals))
print(animals.values())
 