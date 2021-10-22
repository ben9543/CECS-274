from Interfaces import Set
from DLList import DLList
import numpy as np

class ChainedHashTable(Set):
    class Node() :
        def __init__(self, key, value) :
            self.key = key
            self.value = value

    def __init__(self, dtype=DLList) :
        self.dtype = dtype
        self.d = 1
        self.t = self.alloc_table(2**self.d)
        self.z = 193759204821
        self.w = 31
        self.n = 0

    def alloc_table(self, n: int):
        t = np.zeros(n, dtype=np.object)
        for i in range(n):
            t[i] = self.dtype()
        return t


    def hash(self, key : int) -> int :
        return self.z * hash(key) % (2**self.w) >> (self.w - self.d) 

    def size(self) -> int:
        return self.n
        
    def find(self, key : object) -> object :
        for y in self.t[self.hash(key)]:
            if y.key == key: return y.value
        return None
        
    def add(self, key : object, value : object) :
        if self.find(key) != None: return False
        if self.n+1 > len(self.t): self.resize()
        self.t[self.hash(key)].append(self.Node(key, value))
        self.n += 1
        return True

    def remove(self, key : int)  -> object:
        l = self.t[self.hash(key)]
        for y in l:
            if y.key == key:
                l.remove(key)
                self.n-=1
                if 3*self.n < len(self.t): self.resize()
                return y
        return None
    
    def resize(self):
        # print("Resize called")
        if self.n == len(self.t): self.d+=1
        else: self.d-=1
        a = self.alloc_table(2**self.d)
        for j in range(0, len(self.t)):
            for i in range(0, self.t[j].size()):
                ith_node = self.t[j].get(i)
                a[self.hash(ith_node.key)].append(ith_node)
        self.t = a

    def __str__(self):
        s = "["
        for i in range(len(self.t)):
            for j in range(len(self.t[i])):
                k = self.t[i][j]
                s += str(k.key)
                s += ":"
                s += str(k.value)
                s += ";"
        return s + "]"

'''
• Remove one element from an empty ChainedHashTable
• Search in an empty ChainedHashTable: f ind(2) should return nil
• Add 3 elements: add(1, “f irst”), add(2, “second”), add(3, “fourth”)
• Check that size() returns 3
• find one element, f ind(3) should return “fourth”
• Remove one element: remove(3) and check that size() returns 2.
• Find one element: f ind(3) should return nil
• Add 3 elements: add(3, “third”), add(4, “fourth”), add(5, “f if th”).
• Check that size() returns 5
• Find one element: f ind(3) should return “third”
'''

c = ChainedHashTable()
print(c.remove(1))
print(c.find(2))
c.add(1, "First")
c.add(2, "Second")
c.add(3, "Fourth")
print(c.size())
print(c.find(3))
print(c)
# c.remove(1)