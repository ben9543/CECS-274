from BinarySearchTree import BinarySearchTree
from Interfaces import Set


class BinarySearchTreeWithDuplication(Set):

    def __init__(self, nil=None):
        self.binaryTree = BinarySearchTree()
        self.n = 0
        
    def size(self) -> int:
        return self.n 

    def find(self, x: object) -> object:
        return self.binaryTree.find_eq(x)

    def add(self, key : object, value : object) -> bool:
        l = self.find(key)
        if(l is not None):
            #   Add new node to the list
            l.v.append(value)
        else:
            #   Create new list
            newList = [value]
            self.binaryTree.add(key, newList)
        self.n+=1
        
    def remove(self, x : object) -> bool:
        pass
        # return self.binaryTree.remove(x)
     
q = BinarySearchTreeWithDuplication()
q.add(1, "a")
q.add(1, "b")
q.add(2, "c")
q.add(3, "d")
q.add(3, "e")

print(q.find(1).v, q.find(2).v, q.find(3).v)