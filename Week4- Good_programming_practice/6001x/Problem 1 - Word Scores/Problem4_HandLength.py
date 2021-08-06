# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:43:20 2021

@author: SRI
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
	
    leng = sum(hand.values())
    return leng