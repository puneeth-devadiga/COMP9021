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


""" Similar to delete , but deletes particular element from heap """
def delete_element(heap, element):
        if heap.is_empty():
            raise EmptyPriorityQueueError('Cannot delete element from empty priority queue')

        if element not in heap._data:
            raise EmptyPriorityQueueError('Element does not exist in the heap')

        element_to_delete_index = heap._data.index(element)
        heap._data[element_to_delete_index], heap._data[heap._length] = heap._data[pq._length], heap._data[element_to_delete_index]

        heap._length -= 1
        if heap.min_capacity // 2 <= heap._length <= len(heap._data) // 4:
            heap._resize(len(heap._data) // 2)
        heap._bubble_down(element_to_delete_index)
        return element

def get_pq_elements(pq_length):
    return pq._data[1:pq_length]

def set_pq_elements(elements, pq_length):
    pq._data[1:pq_length] = elements

def find_order(heapL):
    result = []

    while True:
        pq_length = pq._length + 1
        for element in heapL:
            # Get Heap elements before delete
            heap_before_delete = get_pq_elements(pq_length)

            delete_element(pq, element)

            # Get Heap elements after delete
            heap_after_delete = get_pq_elements(pq_length-1)

            # reinsert deleted element
            pq.insert(element)

            # Check current elements with before delete list..
            if get_pq_elements(pq_length) != heap_before_delete:
                # reinitialize if heap is not same as before
                set_pq_elements(heap_before_delete, pq_length)
                continue

            # append element to the result and repeat the process for remaining elements.
            result.append(element)
            heapL.remove(element)
            set_pq_elements(heap_after_delete, pq_length)

            pq._length -= 1
            if len(result) == length:
                return result

            break

    return result

# Possibly define some functions
def preferred_sequence():
    heapL=sorted(pq._data[1:pq._length+1], reverse=True)

    if len(heapL) < 3:
        return heapL

    m = find_order(heapL)
    m.reverse()
    return m


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