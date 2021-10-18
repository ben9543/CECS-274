from Interfaces import Stack
import SLLStack

class MaxStack(Stack) :
    def __init__(self):
        self.stack = SLLStack.SLLStack()
        self.max_stack = SLLStack.SLLStack()
        
    def max(self) ->object:
        return self.max_stack.head.x
    
    def push(self, x : object) : 
        self.stack.push(x)
        if self.max_stack.head is None: self.max_stack.push(x)
        else: self.max_stack.push(max(x, self.max_stack.head.x))

    def pop(self) -> object:
        self.max_stack.pop()
        return self.stack.pop()

    def size(self) -> int:
        return self.stack.size()
