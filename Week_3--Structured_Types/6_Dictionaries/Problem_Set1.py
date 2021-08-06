# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:32:15 2021

@author: SRI
"""

'''
#problem set 1
#Suppose x = "pi" and y = "pie". The line of code x, y = y, x will swap the values of x and y, resulting in x = "pie" and y = "pi".

#True



def f(x):
    while x > 3:
        f(x+1)

For any value of x, all calls to f are guaranteed to never terminate.

False


Problem 1-3
1.0/1.0 point (graded)
A Python program always executes every line of code written at least once.

False

Problem 1-4
1.0/1.0 point (graded)
Suppose you have two different functions that each assign a variable called x. Modifying x in one function means you always modify x in the other function for any x.

False


Problem 1-5
0.0/1.0 point (graded)
The following code will enter an infinite loop for all values of i and j.

while i >= 0:
    while j >= 0:
        print(i, j)
        
False


Problem 1-6
1.0/1.0 point (graded)
It is always possible and feasible for a programmer to come up with test cases that run through every possible path in a program.

False

Problem 1-7
1.0/1.0 point (graded)
Assume f() is defined. In the statement a = f(), a is always a function.

False

Problem 1-8
1.0/1.0 point (graded)
A program that keeps running and does not stop is an example of a syntax error.

False

Problem 1-9
1.0/1.0 point (graded)
Consider the following function.
def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)

A new object of type list is created for each recursive invocation of f

True

Problem 1-10
0.0/1.0 point (graded)
A tuple can contain a list as an element.

True




