# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, sample

from priority_queue_adt import *
from copy import deepcopy


# Possibly define some functions
    
def preferred_sequence():
    # Replace pass above with your code (altogether, aim for around 24 lines of code)

    sorted_copy = [pq._data[x] for x in range(1, pq._length + 1)]
    sorted_copy.sort(reverse=True)

    preserved_copy = []
    copy_after_delete = []
    temp_compare = []
    preferred_list = []

    n = 0
    count = 0

    length = deepcopy(pq._length)

    while n <= length:
        n += 1
        
        for i in range(len(sorted_copy)):
            preserved_copy = [pq._data[x] for x in range(1, len(pq) + 1 - count)]

            #delete sorted_copy[i]
            for j in range(len(pq._data)):
                if pq._data[j] == sorted_copy[i]:
                    del_index = j
            #del_index = pq._data.index(sorted_copy[i]) TRY THIS 
            

            if pq.is_empty():
                raise EmptyPriorityQueueError('Cannot delete element from empty priority queue')
            pq._data[del_index], pq._data[pq._length] = pq._data[pq._length], pq._data[del_index]
            pq._length -= 1
            if pq.min_capacity // 2 <= pq._length <= len(pq._data) // 4:
                pq._resize(len(self._data) // 2)
            pq._bubble_down(del_index)

            copy_after_delete = [pq._data[x] for x in range(1, len(pq) - count)]
            
            #insert(sorted_copy[i])
            if pq._length + 1 == len(pq._data):
                pq._resize(2 * len(pq._data))
            pq._length += 1
            pq._data[pq._length] = sorted_copy[i]
            pq._bubble_up(pq._length)

            temp_compare = [pq._data[x] for x in range(1, len(pq) - count)]

            if temp_compare != preserved_copy:
                temp_compare = preserved_copy
                continue
            else:                
                preferred_list.append(preserved_copy[i])
                pq._data[1:pq._length] = copy_after_delete
                pq._length -= 1
                count += 1
                if len(preserved_copy) == length:
                    pass
                break
            
    return preserved_copy
try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                                                             'no greater than 100: '
                                             ).split()
                       ]
    if for_seed < 0 or length > 100:
        raise ValueError
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()    
seed(for_seed)
L = sample(list(range(length * 10)), length)
pq = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[ : len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())

