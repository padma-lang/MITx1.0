# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:27:53 2021

@author: SRI
"""
balance = 42; 
annualInterestRate = 0.2; 
monthlyPaymentRate = 0.04

for i in range(12):
    balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))
print("Remaining balance:", round(balance, 2))