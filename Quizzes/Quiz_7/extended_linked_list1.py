# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        oddhead = None
        evenhead =  None
        lastodd = None
        lasteven = None

        current_node = self.head

        loop_node = self.head
        
        while loop_node:
            current_node = loop_node
            
            if current_node.value%2 != 0:
                if oddhead == None:
                    oddhead = lastodd = current_node
                else:
                    lastodd.next_node = current_node
                    lastodd = current_node
            else:
                if evenhead == None:
                    evenhead = lasteven = current_node
                else:
                    lasteven.next_node = current_node
                    lasteven = current_node
                    
            '''
            print(current_node.value)
            print(current_node.next_node.value)
            '''
            
            loop_node = loop_node.next_node
            

        if oddhead != None:
            self.head = oddhead
        else:
            self.head = evenhead
        
        if lastodd != None and evenhead != None:
            lastodd.next_node = evenhead

        if lasteven != None:            
            lasteven.next_node = None
