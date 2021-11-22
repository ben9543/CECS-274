from BinarySearchTree import BinarySearchTree
from Interfaces import Set


class BinarySearchTreeWithDuplication(Set):

    def __init__(self, nil=None):
        self.binaryTree = BinarySearchTree()
        self.n = 0
        
    def size(self) -> int:
        return self.n 

    def find(self, x: object) -> object:
        l = self.binaryTree.find_eq(x)
        if l is not None:
            return l.v
        return l

    def add(self, key : object, value : object) -> bool:
        l = self.find(key)
        print(l)
        if(l is not None):
            #   Add new node to the list
            l.append(value)
        else:
            #   Create new list
            newList = [value]
            self.binaryTree.add(key, newList)
        self.n+=1
        
    def remove(self, x : object) -> bool:
        return self.binaryTree.remove(x)
    
a = BinarySearchTreeWithDuplication()
a.add(1, "a")
a.add(1, "b")
a.add(1, "c")
a.add(2, "d")
a.add(3, "e")
a.add(3, "z")
print(a.find(1).__str__(), "a,b,c")
print(a.find(2).__str__(), "d") 
print(a.find(3).__str__(), "e,z")