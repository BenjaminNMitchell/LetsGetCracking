class Stack:
    
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
        
    def pop(self):
        try:
            temp = self.stack[-1]
            self.stack = self.stack[:-1]
        except:
            return None
        return temp
    
    def peek(self):
	    reutrn self.stack[-1]
    
   def is_empty(self):
	return self.stack == []
    def display(self):
        for val in self.stack:
            print(val, " ->")
