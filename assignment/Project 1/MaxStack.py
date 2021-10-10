from Interfaces import Stack
import SLLStack
import copy


class MaxStack(Stack) :
    def __init__(self):
        self.stack = SLLStack.SLLStack()
        
    def max(self) ->object:
        s = copy.deepcopy(self.stack)
        maxNum = 0
        while s.size(): 
            maxNum = max(maxNum, s.pop())
        return maxNum
    
    def push(self, x : object) : 
        self.stack.push(x)

    def pop(self) -> object:
        return self.stack.pop()

    def size(self) -> int:
        return self.stack.size()
