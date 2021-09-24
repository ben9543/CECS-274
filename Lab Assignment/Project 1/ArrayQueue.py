import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
        
    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)
    
    def resize(self):
        b = self.new_array(max(1, self.n * 2))

        for i in range(0,self.n):
            b[i] = self.a[i+self.j % len(self.a)]
        self.a = b
        self.j = 0

    def add(self, x : np.object) :
        if self.n+1 > len(self.a) :
            self.resize()
        self.a[self.j+self.n%len(self.a)] = x
        self.n += 1
        return True
        
    def remove(self) -> np.object :
        x = self.a[self.j]
        self.a[self.j] = None # Make value null
        self.j = self.j+1 % len(self.a)
        self.n -= 1
        if len(self.a) >= 3*self.n: self.resize()
        return x

    def size(self) :
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x

