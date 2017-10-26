"""A Simple Queue Object."""

class Queue:

    def __init__(self):
        "Initilize a Queue object."""
        self.head = None
        self.tail = None

    def add(self, node):
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = self.tail

    def remove(self):
        if self.head is None:
            raise RuntimeError("Queue is empty")
        else:
            temp = self.head
            self.head = temp.next
            return temp

    def is_empty(self):
        return self.head is None

    def peak(self):
        return self.head

