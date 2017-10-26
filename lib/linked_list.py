"""A simple Linked List class"""

from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, node):
        node.next = self.head
        self.head = node
    
    def pop(self):
        temp = self.head
        self.head = temp.next
        return temp
    
    def display(self, limit=None):
        ptr = self.head
        print("LinkedList Size: {}".format(self.size))
        counter = 0
        while ptr is not None:
            if limit is not None and counter > limit:
                break
            print(ptr)
            if ptr.next is not None:
                print(" -> ")
            ptr = ptr.next
            counter += 1
            
    def __next__():
        ptr = ll.head()
        while ptr is not None:
            yield ptr
            ptr = ptr.next
            