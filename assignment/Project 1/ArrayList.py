import numpy as np
from Interfaces import List

class ArrayList(List):
    '''
        ArrayList: Implementation of a List interface using Arrays. 
    '''
    def __init__(self):
        '''
        __init__: Initialize the state (array, n and j). 
        '''  
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
        
    def new_array(self, n : int) ->np.array:
        '''
        new_array: Create a new array of size n
        Input:
            n: the size of the new array
        Return:
            An array of size n
        '''
        return np.zeros(n, np.object)
    
    def resize(self):
        '''
        resize: Create a new array and copy the old values. 
        '''
        if (self.n == len(self.a)) or (self.n * 3 <= len(self.a)):
            newArr = self.new_array(max(1, self.n*2))
            for i in range(0, self.n):
                newArr[i] = self.a[i]
            self.a = newArr

    def get(self, i : int) -> object:
        '''
        get: returns the element at position i
        Inputs:
            i: Index that is integer non negative and at most n
        '''
        if i < 0 or i >= self.n: raise IndexError(f"Index {i} is out of bound")
        return self.a[i]

    def set(self, i : int, x : object) -> object:
        '''
        set: Set the value x at the index i.
        Inputs:
            i: Index that is integer non negative and at most n
            x: Object type, i.e., any object 
        '''
        if i < 0 or i >= self.n: raise IndexError(f"Index {i} is out of bound")
        y = self.a[i]
        self.a[i] = x
        return y

    def append(self, x : object) :  
        self.add(self.n, x)
        
    def add(self, i : int, x : object) :
        '''
            add: shift one position all the items j>=i, insert an element 
            at position i of the list and increment the number of elements 
            in the list
            Inputs:
                i: Index that is integer non negative and at most n
                x: Object type, i.e., any object
        '''
        if i < 0 or i > self.n: raise IndexError(f"Index {i} is out of bound")
        self.resize()

        if i < self.n/2: 
            self.j = self.j-1%len(self.a)
            for k in range(0, i):
                self.a[(self.j + k + 1) % len(self.a)] = self.a[(self.j +k) % len(self.a)]
        else:
            for k in range(self.n, i, -1):
                self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
        self.a[(self.j + i) % len(self.a)] = x
        self.n += 1
    
    def remove(self, i: int) -> object:  # Modify
        try:
            if i < 0 or i >= self.n:
                raise Exception()

            x = self.a[(self.j + i) % len(self.a)]

            if i < self.n/2:
                for k in range(i, 0, -1):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]

                self.j = (self.j + 1) % len(self.a)
            else:
                for k in range(i, self.n - 1):
                    self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]

            self.n -= 1

            if len(self.a) >= 3 * self.n:
                self.resize()

            return x
        except Exception:
            raise IndexError()


    def size(self) -> int:
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        s += f"] {self.n} : {self.j}"
        return s

    def __getitem__(self, i) -> object:
        '''
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input: 
                i: positive integer less than n
            Return: the item at index i
        '''
        if isinstance(i, slice):
            return [self.get(i) for i in range(i.start, i.stop)]
        else:
            return self.get(i)


    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator +=1
        else:
             raise StopIteration()
        return x

'''
arraylist = ArrayList()
arraylist.append("a")
arraylist.append("b")
arraylist.append("c")
arraylist.append("d")
arraylist.append("e")
arraylist.append("f")
arraylist.append("g")
arraylist.append("h")
'''