# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 19:11:30 2021

@author: SRI
"""

class coordinates(object):
    def __init__(self,x,y):
        self.x =x
        self.y = y
    
    def distance(self,other):
        '''this is other coordinate'''
        d1 = (self.x - other.x)**2
        d2 = (self.y- other.y)**2
        return (d1 +d2)**0.5
    def __str__(self):
        return "<" + str(self.x)+','+str(self.y)+">"
    def __sub__(self,other):
        return (self.x -other.x,self.y-other.y)
    def __len__(self):
        
        return len(str(self.x))
    
        
        
        

x1= coordinates(2,3)
print(x1.x)

origin = coordinates(1,2)
print(origin.x)

print(x1.distance(origin))

print(x1)

z = x1 -origin
print(z)






