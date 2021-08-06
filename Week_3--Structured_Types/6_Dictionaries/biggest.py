# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 10:26:50 2021

@author: SRI
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    counter = 0
    result = None
    
    if aDict == {}:
        return None
    else:
        for x in aDict.keys():
            if len(aDict[x])> counter:
                result = x         
                
        return result
        
        
print(biggest(animals))
                            


