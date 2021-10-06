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
        self.queue.add(x) 

    def remove(self) -> object:
        ranNum = random.randint(0, self.queue.n-1)
        modNum = ranNum % len(self.queue.a)
        temp = self.queue.a[self.queue.j % len(self.queue.a)]
        self.queue.a[self.queue.j % len(self.queue.a)] = self.queue.a[modNum]
        self.queue.a[modNum] = temp
        temp = None
        x = self.queue.remove()

        [1,2,3, None, None]
        return x
    
    def size(self) -> int:
        return self.queue.size()
