memo = {}
def fibo(x):
    if x in memo:
        return memo[x]
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x > 2:
        val = fibo(x - 1) + fibo(x - 2)
        memo[x] = val
    return val

for i in range(1, 10000001):
    print(f'fibo series{i} is {fibo(i)}')
