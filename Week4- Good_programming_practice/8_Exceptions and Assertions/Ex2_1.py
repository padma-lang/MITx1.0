# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 17:43:00 2021

@author: SRI
"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
         item /= denom
         return item
    except ZeroDivisionError:
        return 0
        
print(fancy_divide([0, 2, 4], 0))
        

