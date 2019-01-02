
from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        new_list = set()
        self.node = self.head
        new_list.add(self.node)
        if self.next_node not in new_list:
            new_list.add(self.next_node)
            self.node = self.next_node
            self.next_node = self.next_node.next_node
        
        
