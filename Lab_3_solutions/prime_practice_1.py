



'''
Finds all sequences of consecutive prime 5-digit numbers, say (a, b, c, d, e, f), such that
b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.
'''
from math import sqrt

def is_prime(num):
    for i in range(2, round(sqrt(num))+1):
        if num%i == 0:
            return False
    return True

print()

print('The solutions are:\n')

for i in range(10001, 100000, 2):
    check = []
    for x in range(i, i + 31):    
        check.append(is_prime(x))        
        if check.count(True) > 6:
            break
    if check.count(True) == 6 and is_prime(i) == is_prime(i+2) == is_prime(i+6) == is_prime(i+12) == is_prime(i+20) == is_prime(i+30) == True:
        print(i,'' ,i+2,'' ,i+6,'' ,i+12,'' ,i+20,'' ,i+30)






