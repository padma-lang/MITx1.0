# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:20:55 2021

@author: SRI
"""

'''
Exercise 2
1/1 point (graded)
ESTIMATED TIME TO COMPLETE: 5 minutes

Consider the following code specification:

def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   
   
set1 is an empty set; set2 is an empty set-correct
set1 is an empty set; set2 is of size greater than or equal to 1-correct
set1 is of size greater than or equal to 1; set2 is an empty set-correct
set1 and set2 are both nonempty sets which do not contain any objects in common
correct
set1 and set2 are both nonempty sets which contain objects in common-correct