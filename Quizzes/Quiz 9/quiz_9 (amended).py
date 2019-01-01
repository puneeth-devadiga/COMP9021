# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children, and
# - the sum of the nodes along all of T*'s branches is equal to M.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randrange

from binary_tree_adt import *

def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)


def expand_tree(tree):
    #Assigning max_sum to x
    max_sum = find_max_sum(tree)
    #print(f'max value {x}')
    rearrange(tree, max_sum)
    
    
def rearrange(tree, max_sum):    
    if tree.value is None:
        return 0
    
    if tree.left_node.value is None and (max_sum - tree.value) != 0:
        #Creating left tree with {max_sum - tree.value}
        tree.left_node = BinaryTree(max_sum - tree.value)       
    else:
        rearrange(tree.left_node, max_sum - tree.value)
        
    if tree.right_node.value is None and (max_sum - tree.value) != 0:
        # Creating right tree with {max_sum - tree.value}
        tree.right_node = BinaryTree(max_sum - tree.value)       
    else:
        rearrange(tree.right_node, max_sum - tree.value)
        

def find_max_sum(tree):
    if not tree.value and tree.value != 0:
        return 0
    
    if tree.left_node is None and tree.right_node is None:
        return tree.value
    else:
        return tree.value + max(find_max_sum(tree.left_node),find_max_sum(tree.right_node))
        
# Possibly define other functions
                
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()]
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
expand_tree(tree)
print('Here is the expanded tree:')
tree.print_binary_tree()




