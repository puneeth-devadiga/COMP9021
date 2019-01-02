
#Written by Puneeth S.Devadiga for COMP9021


from copy import deepcopy

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLinkedList:
    def __init__(self, L = None, key = lamda x:x):

        if L is None:
            self.head = None
            self.tail = None
            return
        
