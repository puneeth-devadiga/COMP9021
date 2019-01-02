



'''
Finds all sequences of consecutive prime 5-digit numbers, say (a, b, c, d, e, f), such that
b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.
'''
a= 136
b = 123456
from math import sqrt

def is_prime(num):
    for i in range(2, round(sqrt(num))+1):
        if num%i == 0:
            return False
    return True

count = []
for i in range(a, b+1):
    if is_prime(i) == True:
        count.append(i)

print('No of primes between a and b:', len(count))
    
