# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 19:31:58 2021

@author: SRI
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):

    sum = 0
    for i in aDict.values():
        
        sum += len(i)
    return sum


print(how_many(animals))
print(animals)
