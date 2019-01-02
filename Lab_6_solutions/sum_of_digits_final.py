








import sys


def solve(d, s):
    if s < 0:
        return 0
    if d == 0:
        if s == 0:
            return 1
        return 0
    return solve(d//10, s) +\
           solve(d//10, s - d%10)

try:
    s = int(input('Enter Sum: '))
except ValueError:
    print('Incorrect input')
    sys.exit()
try:
    d = abs(int(input('Enter digits: ')))
except ValueError:
    print('Incorrect input')
    sys.exit()
nb_of_solutions = solve(d, s)

print('There are {} solutions.'.format(nb_of_solutions))
