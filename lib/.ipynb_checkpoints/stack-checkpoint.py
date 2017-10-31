class Stack:
    
    def __init__(self):
        self.stack = []
        self.min = None
    
    def push(self, value):
        self.stack.append(value)
        if value < self.min[0]:
            self.min = [value]
        elif value == self.min[0]:
            self.min.append(value)
            
    def pop(self):
        try:
            
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
        except:
            return None
        return temp
    
    def peek(self):
	    reutrn self.stack[-1]
        
    def get_min(self):
        return self.min[0]
    
    def is_empty(self):
	    return self.stack == []
    
    def display(self):
        for val in self.stack:
            print(val, " ->")
