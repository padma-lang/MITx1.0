# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:43:27 2021

@author: SRI
"""

'''
Problem 5
20.0/20.0 points (graded)
Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    
    
    
    def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    # Your code here
    sortList=[]
    outList=[]
    # Place values into a list
    #If there is only one of the values, then add to list. Otherwise, don't
    sortList = list(aDict.values())
    #need a loop to remove all instances of a duplicate
    #the length of the list will go down every time I remove an element
    #for i in range(len(sortList)):
    #    while sortList[i] in sortList[i+1:len(sortList)]:
    #        sortList.remove(sortList[i])
    #for i in range(len(sortList)):
    for i in sortList:
        if sortList.count(i) > 1: #if the item i appears in the list  > 1
            while i in sortList: #while that item is in the list
                sortList.remove(i) #remove that item!
   
    for k, v in aDict.items():
        if v in sortList:
            outList.append(k)
           
    outList.sort()
    return outList
          