# Written by Eric Martin for COMP9021


'''
Finds all triples of positive integers (i, j, k) such that i, j and k are two digit numbers,
i < j < k, every digit occurs at most once in i, j and k, and the product of i, j and k
is a 6-digit number consisting precisely of the digits that occur in i, j and k.
'''


# If i, j and k are numbers in the range [10, 99], i < j < k, and every digit occurs at most once
# in i, j and k, then 10 <= i <= 76, j <= 87, and k <= 98. 

for i in range(10, 99):
    for j in range(i+1, 99):
        for k in range(j+1, 99):
            I = set([int(x) for x in str(i)])
            J = set([int(x) for x in str(j)])
            K = set([int(x) for x in str(k)])

            union = I|J|K
            if len(union) != 6:
                continue

            P = set([int (x) for x in str(i * j * k)])

            if union == P:
                print(f'{i} X {j} X {k} = {i*j*k}')
