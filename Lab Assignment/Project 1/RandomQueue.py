import random 
from Interfaces import Queue 
import ArrayQueue


class RandomQueue(Queue):
    def __init__(self):
        self.queue = ArrayQueue.ArrayQueue()


    def add(self, x : object):
        '''
            add: Add the value x to the Queue
            Inputs:
                x: Object type, i.e., any object
        '''
        self.queue.add(random.randint()) 

    def remove(self) -> object:
        '''
            remove: remove the next (previously added) value, y, from the
                    Queue and return y. The Queue’s queueing discipline 
                    decides which element should be removed.
            Return: Object type
        '''
        x = self.queue.remove()
        return x
    
    def size(self) -> int:
        return self.queue.size()


r = RandomQueue()
r.add()
r.add()
print(r)
r.remove()