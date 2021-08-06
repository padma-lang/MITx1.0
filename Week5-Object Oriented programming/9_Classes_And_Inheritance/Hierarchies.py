# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:39:24 2021

@author: SRI
"""

class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self,newage):
        self.age = newage
        
    def set_name(self,newname =''):
        self.name = newname
    
    def __str__(self):
        return "animal: "+ str(self.name)+ ":" +str(self.age)

class Cat(Animal):
    def speak(self):
        print("meow")
    
    def __str__(self):
        return "cat: "+ str(self.name)+ ':' +str(self.age)
    
class Rabbit(Animal):
    def speak(self):
        print("keww")
    
    def __str__(self):
        return "Rabbit: "+ str(self.name)+ ':' +str(self.age)


class Rabbit(Animal):
    def speak(self):
        print("keww")
    
    def __str__(self):
        return "Rabbit: "+ str(self.name)+ ':' +str(self.age)
        
    
    
        