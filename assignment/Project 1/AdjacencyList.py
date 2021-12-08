"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue

class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()
            
    def add_edge(self, i : int, j : int):
        self.adj[i].append(j)
        
    def remove_edge(self, i : int, j : int):
        if len(self.adj[i]) == 0: return
        for k in range(len(self.adj[i])):
            # print(self.adj[i].get(k))
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return
                
    def has_edge(self, i : int, j: int) ->bool:
        for k in self.adj[i]:
            if k == j: return True
        return False
        
    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, j) -> List:
        out = ArrayStack.ArrayStack()
        for i in range(self.n):
            if self.has_edge(i, j): out.push(j)
        return out

    def bfs(self, r :int):
        pass

    def dfs(self, r :int):
        pass

    
    def distance(self, r : int, dest: int):
        pass

    def size(self) -> int :
        return self.n
                      
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s

'''
g = AdjacencyList(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g.dfs(0,1))
'''