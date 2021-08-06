# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 19:31:45 2021

@author: SRI
"""

lyrics = ['she','loves','the','the','world','she','is','love']



def counter(list1):
    s1 = {}
    
    for word in list1:
        if word in s1:
            s1[word]+=1
            
        else:
            s1[word]= 1
    return s1

print(counter(lyrics))

b = counter(lyrics)

def most_common_words(b):
    values = b.values()
    
    best = max(values)
    
    words = []
    for k in b:
        if b[k]== best:
            words.append(k)
            
    return (words,best)

print(most_common_words(b))

def words_often(b,mintimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(b)
        

        if temp[1] >= mintimes:
            result.append(temp)
            
            
            
            print(f'before b is {b}')
                
            for w in temp[0]:
                print(f' w is {w}')
                print(f' bw is {b[w]}')
                del (b[w])
                print(f'b is {b}')
                
           
        else:
            done = True
    return result

print(words_often(b, 2))
    
                         
