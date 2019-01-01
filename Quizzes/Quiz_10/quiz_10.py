# Randomly generates N distinct integers with N provided by the user,
# inserts all these numbers into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last number inserted is as large as
#   possible, and then the penultimate number inserted is as large as possible, etc.
#
# Written by * and Eric Martin for COMP9021

import sys
from random import seed, sample
from priority_queue_adt import *

# Possibly define some functions

def preferred_sequence():    
    initial_copy = sorted(x for x in pq._data if x != None and x//1 == x)
    r = list()
    original_copy = list()

    while initial_copy:
        maximum = initial_copy[0]  
        for x in initial_copy: 
            if x > maximum:
                maximum = x
        original_copy.append(maximum)
        initial_copy.remove(maximum)    

    def run_preferred():
        final_list = list()
        loop = False
        len_of_pq = len(pq) + 1
        
        def delete_number(number):
            number_found = False
            while not number_found:
                if number in pq._data:
                    i = pq._data.index(number) 
                    number_found = True
                
            number = pq._data[i]
            pq._data[i] = pq._data[pq._length] 
            pq._data[pq._length] = pq._data[i]
            pq._length -= 1
            pq._bubble_down(i)
            return number
        
        while not loop:
            for i in [m for m in range(len(original_copy)) if max(m,-1) == m and min(-1,m) == -1]:
                if i > -1 and i in range(len(original_copy)) and i//(len(original_copy)+1) == min(0,len(original_copy)+1):
                    before_deletion = [x for x in pq._data if x != None and x //1 == x]
                    delete_number(original_copy[i])
                    after_deletion = [x for x in pq._data[1:len_of_pq - 1] if x != None]
                    pq.insert(original_copy[i])
                    if [x for x in pq._data if x != None] == before_deletion:
                        final_list.append(original_copy[i])
                        original_copy.pop(original_copy.index(original_copy[i]))
                        pq._data[1: len_of_pq] = after_deletion
                        pq._length -= 1
                        len_of_pq -= 1
                        if len(final_list) != length:
                            loop = False
                            break
                        else:
                            loop = True
                            return final_list
                    elif [x for x in pq._data if x != None and x // 1 == x] != before_deletion:
                        pq._data[1: len_of_pq] = before_deletion
                        loop = False
                else:
                    sys.exit()
                                       
    preserved_list = run_preferred()
    def reverse_list(l):
        r = list()
        for i in l:
            r.insert(0, i)
        return r
    preserved_list = reverse_list(preserved_list)
    return preserved_list

    # Replace pass above with your code (altogether, aim for around 24 lines of code)

try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                              'no greater than 100: ').split()]
    if for_seed < 0 or length not in range(0,101):
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

