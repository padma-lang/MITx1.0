# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 13:31:36 2021

@author: SRI
"""

def genPrimes():
    primes = [2]
    yield primes[0]
    guess = 3
    while True:
        if all(guess%x != 0 for x in primes):
            primes.append(guess)        
        if guess == primes[-1]:
            yield primes[-1]
        guess += 2
        
