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



import sys
from random import seed, randrange

from stack_adt import *
from datetime import datetime
startTime = datetime.now()


def display_grid():
    for a in range(len(grid)):
        print('   ', ' '.join(str(grid[a][b]) for b in range(len(grid[0]))))


try:
    for_seed, bound, I, J, target = [int(x) for x in input('Enter five integers: ').split()]
    if bound < 1 or I not in range(10) or J not in range(10) or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(bound) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()

final_path = None

s = 0
for p in range(len(grid)):
    for q in range(len(grid[0])):
        s = s + grid[p][q]

if grid[I][J] == target:
    final_path = [(I,J)]
    
elif s >= target:
    directions = {'W':[0,-1],'S':[1,0],'E':[0,1], 'N':[-1, 0]}

    explore = {'W' :['S','N','W'],'S' :['E','W','S'],'E' :['N','S','E'],'N':['W','E','N']}
    stack = Stack()

    for direction in directions:
        new_i = I + directions[direction][0]
        new_j = J + directions[direction][1]

        if new_i in (0,1,2,3,4,5,6,7,8,9) and new_j in (0,1,2,3,4,5,6,7,8,9):
            if (grid[I][J] + grid[new_i][new_j]) > target:
                continue
            stack.push([direction, [(I,J),(new_i,new_j)], (grid[I][J]+grid[new_i][new_j]) ])
        else: 
            continue
        
    while stack.is_empty() != True and not final_path:
        direction, keep_track, value = stack.pop()
        
        if target in [value]:
            final_path = keep_track
            break
        
        i = keep_track[-1][0]
        j = keep_track[-1][1]
        
        for z in explore[direction]:
            new_i = i + directions[z][0]
            new_j = j + directions[z][1]
            
            if new_i not in (0,1,2,3,4,5,6,7,8,9) or new_j not in (0,1,2,3,4,5,6,7,8,9):
                continue
            else:
                addable = value + grid[new_i][new_j]
                
                if addable > target or (new_i,new_j) in keep_track:
                    continue
                
                keep_track_2 =  keep_track.copy()
                keep_track_2.append((new_i,new_j))
                stack.push([z, keep_track_2, addable])

if not final_path:
    print(f'There is no way to get a sum of {target} starting from ({I}, {J})')
else:
    print('With North as initial direction, and exploring the space clockwise,')
    print(f'the path yielding a sum of {target} starting from ({I}, {J}) is:')
    print(final_path)

print (datetime.now() - startTime)

