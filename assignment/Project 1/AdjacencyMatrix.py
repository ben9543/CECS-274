"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack

class AdjacencyMatrix(object):
    def __init__(self, n):
        self.n = n
        self.a = np.zeros([n, n], np.bool_)

    # Lab7          
    def add_edge(self, i, j):
        self.a[i][j] = True

    # Lab7 
    def remove_edge(self, i, j):
        self.a[i][j] = False

    # Lab7 
    def has_edge(self, i, j):
        return self.a[i][j]

    # Lab7 
    def out_edges(self, i):
        arr = []
        for k, d in enumerate(self.a[i]):
            if d: arr.append(k)
        return arr
    
    # Lab7 
    def in_edges(self, i):
        arr = []
        for k, d in enumerate(self.a):
            if d[i]: arr.append(k)
        return arr
    
    # Not mentioned 
    def in_degree(self, i):
        pass
        
    # Not mentioned 
    def out_degree(self, i):
        pass
    
    # Not mentioned 
    def size(self) -> int :
        return self.n
                  
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.has_edge(i,j):
                    s += f"{i,j}"
        return s

'''
g = AdjacencyMatrix(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g.dfs(0,1))
'''
