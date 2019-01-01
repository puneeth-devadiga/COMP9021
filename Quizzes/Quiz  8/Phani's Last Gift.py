# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north,
# always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Eric Martin for COMP9021

import sys
from random import seed, randrange
from stack_adt import *

from datetime import datetime
startTime = datetime.now()


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))


def explore_depth_first(x, y, target):
    directions = {'North': (-1, 0),'South': (1 , 0),'East':  (0 , 1),'West':  (0 ,-1)}

    movable_directions = {'North':['North','East','West'], 'South':['South','West','East'],'East' :['East','South','North'],'West' :['West','North','South'], 'Initial':['North','East','South','West']}
    
    discovered = []
    discovered.append([[(x,y)], 'Initial', [grid[x][y]] ])
    possible_coordinates = set()
    
    for i in range(10):
        for j in range(10):
            possible_coordinates.add((i,j))

    row_sum = [sum(x) for x in grid]
    if sum(row_sum) < target:
        return None

    while discovered != []:
        traced, d, addition = discovered.pop()
        
        if max(addition) == target:
            return traced
        
        m1 = traced[-1][0]
        n1 = traced[-1][1]
        
        for z in reversed(movable_directions[d]):
            m2 = m1 + directions[z][0] ; n2 = n1 + directions[z][1]
            
            mn=set()
            mn.add((m2,n2))
            if mn.issubset(possible_coordinates) == False:
                continue           
            addable = max(addition) + grid[m2][n2]
            if addable > target:
                continue
            
            if (m2,n2) in set(traced):
                continue
            
            traced_2 =  traced.copy(); traced_2.append((m2,n2))
            addition_2 = addition.copy(); addition_2.append(addable)
            discovered.append([traced_2, z, addition_2])

            # Replace pass above with your code
            
try:
    for_seed, bound, x, y, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or x not in range(10) or y not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = explore_depth_first(x, y, target)
if not path:
    print(f'There is no way to get a sum of {target} starting from ({x}, {y})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({x}, {y}) is:')
    print(path)

print (datetime.now() - startTime)

