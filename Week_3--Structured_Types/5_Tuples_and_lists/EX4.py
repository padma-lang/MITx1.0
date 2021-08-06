# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 16:44:21 2021

@author: SRI
"""

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList


print(aList is bList)


print(aList)



print(bList)


cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
        dList.append(num)
        print(cList == dList)


print(cList is dList)
 
cList[2] = 20
print(cList)


print(dList)

