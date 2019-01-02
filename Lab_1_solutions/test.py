from random import randrange

L = [randrange(20) for i in range(10)]

print(L)

interval = [] * 4
for i in range(len(L)):
    interval[L[i]//5] += 1

print(intervals)
