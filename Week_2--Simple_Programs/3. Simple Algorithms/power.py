# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:37:48 2021

@author: SRI
"""

'''iterative power'''




def iterpower(base,exp):
    n = 1
    while exp >0:
        n = (n * base)
        exp -=1
    return n
           
print(iterpower(3,2))



'''recursive power'''

def recpower(base,exp):
    if exp == 0:
        return base * exp +1
    else:
        return base * recpower(base, exp-1)
    
print(recpower(3,2)) 
    
    
    
            
        
    
     
                
         


    
        
        
    
         
    
    
    

