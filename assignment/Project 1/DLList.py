from Interfaces import List
import numpy as np


class DLList(List):
    class Node:
        def __init__(self, x : np.object) :
            self.next = None
            self.prev = None
            self.x = x

    def __init__(self) :
        self.dummy = DLList.Node("")
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.n = 0
   
    def get_node(self, i : int) -> Node:
        p = None
        if i < self.n/2:
            # Start from dummy.next
            p = self.dummy.next
            for _ in range(0,i):
                p = p.next
        else:
            # Start from dummy
            p = self.dummy
            for _ in range(0, self.n - i):
                p = p.prev
        return p

    def get(self, i) -> np.object:
        return self.get_node(i).x

    def set(self, i : int, x : np.object) -> np.object:
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add_before(self, w : Node, x : np.object) -> Node:
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        w.prev = u # Same as: u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u
            
    def add(self, i : int, x : np.object)  :
        self.add_before(self.get_node(i), x)

    def _remove(self, w : Node) :
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1

    
    def remove(self, i :int) :
        self._remove(self.get_node(i))

    def size(self) -> int:
        return self.n

    def append(self, x : np.object)  :
        self.add(self.n, x)

    def isPalindrome(self) -> bool :
        p = self.dummy
        ahead = p.next
        before = p.prev
        if self.n%2 == 1: self.n -= 1
        for _ in range(0, self.n):
            if ahead.x == before.x:
                ahead = ahead.next
                before = before.prev
            else:
                return False
        return True

    # Switch each node's prev and next until current node points to self.dummy
    def reverse(self) :
        if self.n == 0 : return
        originalDummy = self.dummy
        curr = self.dummy
        while True:
            prev = curr.prev
            curr.prev = curr.next 
            curr.next = prev
            curr = curr.prev
            if curr == originalDummy: break
            

         
    def __str__(self):
        s = "["
        u = self.dummy.next
        while u is not self.dummy:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"


    def __getitem__(self, i) -> object:
        '''
            __getitem__: Returns the item in the position i in array format, i.e., l[i]
            where l is a list instance
            Input: 
                i: positive integer less than n
            Return: the item at index i
        '''
        if isinstance(i, slice):
            raise IndexError("Not implemented. Please use the references next and prev")
        else:
            return self.get(i)


    def __iter__(self):
        self.iterator = self.dummy.next
        return self

    def __next__(self):
        if self.iterator != self.dummy:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
             raise StopIteration()
        return x

