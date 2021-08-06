# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 09:48:09 2021

@author: SRI
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        print(f'word is :{ans}')
        return ans
            
        
          
        
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))
   
    
print(isPalindrome('sammy'))
