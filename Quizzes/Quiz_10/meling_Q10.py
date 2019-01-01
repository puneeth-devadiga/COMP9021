# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by * and Eric Martin for COMP9021


import sys
from random import seed, sample

from priority_queue_adt import *


# Possibly define some functions

def delete_element(pq, element):
    if pq.is_empty():
        raise EmptyPriorityQueueError('Cannot delete element from empty priority queue')
    for j in range(len(pq._data)):
        if pq._data[j] == element:
            i = j
            break
    element = pq._data[i]
    pq._data[i], pq._data[pq._length] = pq._data[pq._length], pq._data[i]
    pq._length -= 1

    # When the priority queue is one quarter full, we reduce its size to make it half full,
    # provided that it would not reduce its capacity to less than the minimum required.
    if pq.min_capacity // 2 <= pq._length <= len(pq._data) // 4:
        pq._resize(len(pq._data) // 2)
    pq._bubble_down(i)
    return element

def best_order(current_style):
    L_L = []
    n = 0
    pq_length = len(pq) + 1
    while n == 0:
        for i in range(0, len(current_style)):
              A_A = pq._data[1: pq_length]
              delete_element(pq, current_style[i])
              B_B = pq._data[1: pq_length - 1]
              pq.insert(current_style[i])
              if pq._data[1: pq_length] != A_A:
                  pq._data[1: pq_length] = A_A
                  continue
              else:
                  L_L.append(current_style[i])
                  current_style.remove(current_style[i])
                  pq._data[1: pq_length] = B_B
                  pq._length -= 1
                  pq_length -= 1
                  if len(L_L) == length:
                      return L_L
                  break
    return L_L

def preferred_sequence():
    current_style = sorted(pq._data[1: len(pq) + 1])
    current_style.reverse()
    M = best_order(current_style)
    M.reverse()
    return M







    # Replace pass above with your code (altogether, aim for around 24 lines of code)


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
initial_style = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[: len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())

