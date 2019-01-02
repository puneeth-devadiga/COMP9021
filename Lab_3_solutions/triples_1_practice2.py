# Written by Eric Martin for COMP9021


'''
Finds all triples of positive integers (i, j, k) such that i, j and k are two digit numbers,
i < j < k, every digit occurs at most once in i, j and k, and the product of i, j and k
is a 6-digit number consisting precisely of the digits that occur in i, j and k.
'''


# If i, j and k are numbers in the range [10, 99], i < j < k, and every digit occurs at most once
# in i, j and k, then 10 <= i <= 76, j <= 87, and k <= 98. 

a = 50
b = 110

for i in (range(a, b+1)):
    for j in (range(i, b+1)):
        I = set([int(x) for x in (str(i))])
        J = set([int(x) for x in (str(j))])       
        P = set([int(x) for x in (str(i*j))])
        
        if len(I|J|P) != 8:
            continue
        else:
            print(f'{i} X {j} = {i*j}')
            


