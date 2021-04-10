#encoding utf-8

import random
import math

'''
def primalTest(p):
    if p%2 == 0:
        return False
    else:
        i = 3
        sqrt = math.sqrt(p)
        while(i<sqrt):
            if p%i == 0:
                return False
    return True
'''

def primalFermatTest(p):
    if pow(2,p-1)%p != 1:
        return False
    else:
        return True
        
        '''
        if primalTest(p) == True:
            return True
    return False
        '''



def generationLargePrimeNumber(n): # n is the number of bits you wish
    while(True):
        p = random.randint(pow(2,n-1),pow(2,n)-1)
        if primalFermatTest(p) == True:
            break
    return p


