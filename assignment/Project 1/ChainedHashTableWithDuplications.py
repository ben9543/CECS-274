from Interfaces import Set
from DLList import DLList
import ChainedHashTable 

class ChainedHashTableWithDuplications(Set):
    def __init__(self) :
        self.chainHashTable = ChainedHashTable.ChainedHashTable()
        self.n = 0

    def size(self) -> int:
        return self.n
        
    def find(self, key : object) -> object :
<<<<<<< HEAD
        a = []
        if key == None:
            return IndexError
        # Resize
        self.chainHashTable.find(key)
        
    def add(self, key : object, value : object) :
        
        if not self.chainHashTable.add(key, value):
            # add a list
            pass
        else:
            # self.find(key).add(value)
            pass
        
=======
        return self.chainHashTable.find(key)
        
    def add(self, key : object, value : object) :
        node = self.chainHashTable.find(key)
        if node:
            node.append(value)
        else:
            newList = DLList()
            newList.append(value)
            self.chainHashTable.add(key, newList)
>>>>>>> 63a94c57c1e2ef56d44c6449b5c89c0660052530
    
    def remove(self, key : int)  -> object:
        return self.chainHashTable.remove(key)
    
    def __str__(self):
        return self.cht.__str__()

