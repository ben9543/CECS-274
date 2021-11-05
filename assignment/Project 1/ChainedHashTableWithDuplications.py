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
        return self.chainHashTable.find(key)
        
    def add(self, key : object, value : object) :
        node = self.chainHashTable.find(key)
        if node:
            node.append(value)
        else:
            newList = DLList()
            newList.append(value)
            self.chainHashTable.add(key, newList)
    
    def remove(self, key : int)  -> object:
        return self.chainHashTable.remove(key)
    
    def __str__(self):
        return self.cht.__str__()

c = ChainedHashTableWithDuplications()
c.add("a", 1)
r = c.add("a", 2)
print(c.chainHashTable, r)
