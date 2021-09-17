from Interfaces import Stack
import SLLStack


class MaxStack(Stack) :
    def __init__(self):
        self.stack = SLLStack.SLLStack()
        
    def max(self) ->object:
        '''
            Returns the max element
        '''
        pass
    
    def push(self, x : object) : 
        '''
            push: Insert an element in the tail of the stack 
            Inputs:
                x: Object type, i.e., any object
        '''
        pass

    def pop(self) -> object:
        '''
            pop: Remove the last element in the stack 
            Returns: the object of the tail if it is no empty
        '''
        pass

    def size(self) -> int:
        return self.stack.size()
