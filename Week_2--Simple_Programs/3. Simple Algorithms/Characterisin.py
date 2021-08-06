# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 11:22:36 2021

@author: SRI
"""

def isIn(char, aStr):
    
    aStrSorted = sorted(aStr)
    low = 0
    high = len(aStrSorted)
    mid = int( (low + high) / 2)
    

    i = 0
    while i < 50:
        i += 1
        if len(aStr) <= 0:
            return False
            
        if char == aStrSorted[mid]:
            print ("Match! char = " + char + "  in " + str(aStrSorted))
            return True
        if (low == mid or high == mid) and (char != aStrSorted[mid]):
            print ("False")
            return False
        else:
            #print "not here"
            if char > aStrSorted[mid]:
                print ("char '"+ char +"'  is bigger than "+aStrSorted[mid]+", current low = " + str(low) + " , new Low = " + str(mid))
                low = mid
                return isIn(char, aStrSorted[low:high])

            else:
                print ("char '"+ char +"'  is smaller than "+aStrSorted[mid]+", current high = " + str(high) + " , new high = " + str(mid))
                high = mid
                return isIn(char, aStrSorted[low:high])
            

print(isIn('x','sammay'))