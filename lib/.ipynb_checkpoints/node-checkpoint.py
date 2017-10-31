"""A simple Node class"""

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
       
    def __str__(self):
        return "Node Value: {}".format(self.value)


    
class NodeWithPrevMin:
    
    def __init__(self, value, prev_min):
        self.value = value
        self.prev_min = prev_min
        self.next = None
       
    def __str__(self):
        return "Node Value: {} Prev Min: {}".format(self.value,
                                                    self.prev_min)