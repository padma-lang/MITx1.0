# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:53:02 2021

@author: SRI
"""

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
       
        for i in range(len(numbers)):
           
            
            numbers[i] /= denom
           
            
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")
        
        
#print(fancy_divide([0, 2, 4], 1))
print('****************')
#print(fancy_divide([0, 2, 4], 4))

print('****************')
#print(fancy_divide([0, 2, 4], 0))


def fancy_divide1(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")
 
#print(fancy_divide1([0, 2, 4], 1))
print('****************')
fancy_divide1([0, 2, 4], 4)

print(fancy_divide1([0, 2, 4], 0))


def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
print(fancy_divide([0, 2, 4], 1))
print('***********///*')
print(fancy_divide1([0, 2, 4], 4))
print('*********-------')
print(fancy_divide1([0, 2, 4], 0))

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
        
        
        
print(fancy_divide([0, 2, 4], 0))
print('*********-------')

def fancy_divide(list_of_numbers, index):
    try:
        try:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
        finally:
            raise Exception("0")
    except Exception as ex:
        print(ex)
        
print(fancy_divide([0, 2, 4], 0))
print('--------******-------')

def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

#print(fancy_divide([0, 2, 4], 0))


def fancy_divide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError:
            fancy_divide(numbers, len(numbers) - 1)
        else:
            print("1")
        finally:
            print("0")
    except ZeroDivisionError:
        print("-2")
print(fancy_divide([0, 2, 4], 0))