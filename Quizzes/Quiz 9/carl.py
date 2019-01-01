# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children,
# - the sum of the nodes along all of T*'s branches is equal to M, and
# - when leaves in T are expanded to 2 leaves in T*, those 2 leaves receive the same value.
#
# Written by * and Eric Martin for COMP9021

#98 4 3

import sys
from random import seed, randrange

from binary_tree_adt import *
from datetime import datetime
startTime = datetime.now()

def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)
        

def s(node):
    if node.value is None:
        return 0
    else:
        return node.value + max(s(node.left_node), s(node.right_node))

def expand_tree(node,m):
    if node.value is None:
        return 0
    m -= node.value
    if node.left_node.value is None and m > 0:
        node.left_node = BinaryTree(m)
    else:
        expand_tree(node.left_node, m)
    if node.right_node.value is None and m > 0:
        node.right_node = BinaryTree(m)
    else:
        expand_tree(node.right_node, m)
    # Replace pass above with your code
# Possibly define other functions

                
try:
    #for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   #]
    for_seed, for_growth, bound = 0, 5, 6
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()

M = s(tree)
expand_tree(tree,M)
print('Here is the expanded tree:')
tree.print_binary_tree()
print(datetime.now() - startTime)
