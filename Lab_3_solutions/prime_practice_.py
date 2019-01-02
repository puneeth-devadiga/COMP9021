# Written by Eric Martin for COMP9021


'''
Finds all sequences of consecutive prime 5-digit numbers, say (a, b, c, d, e, f), such that
b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.
'''

from math import sqrt

def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
        else:
            return True
  
