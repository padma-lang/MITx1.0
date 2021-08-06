# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 12:38:32 2021

@author: SRI
"""

low = 0
high = 100

print('Please think of a number between 0 and 100!')
while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + ' ?')
    a = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if a == 'c':
        print('Game over. Your secret number was:', str(guess))
        break
    elif a =='l':
        low = guess
        
        
    
    elif a=='h':
        high = guess
       
        
        
    else:
        print('sorry wrong input')
        
'Newton -Raphson'
y = 24.0
epsilon = 0.01
guess = y/2.0
counter =0

while abs(guess*guess -y)>= epsilon:
    
    counter+=1
    guess = guess -(((guess**2)-y)/(2*guess))

print(counter)
print(f'{guess} is the closest square root of {y} using Newton-Raphson')

