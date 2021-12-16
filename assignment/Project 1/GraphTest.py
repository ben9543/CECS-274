import AdjacencyList
import AdjacencyMatrix

'''
#1
Test your program:
• Create a graph with 4 nodes.
• Remove an edge from an empty graph, e.g., remove_edge(2, 3).
• Check if an edge does exists, e.g., has_edge(2, 3).
• Addedges(0,1),(1,2),(2,3),(3,0),(0,2),add_edge(0,1),add_edge(1,2),add_edge(2,3), add_edge(3, 0), add_edge(0, 2).
• Check for the edge (0, 1) and (1, 3). The first one must exist and the second must not exist.
• Compute the in edges of 2, i.e., in_edges(2). It should return 0, 1 in any order.
• Compute the out edges of 0, i.e., out_edges(0). It should return 1, 2 in any order.
• DisplaytheoutputofBFS(0).Theoutputmustbe0,1,2,3or0,2,1,3.
• DisplaytheoutputofDFS(1).Theoutputmustbe0,2,3,1or0,1,2,3.
'''

al = AdjacencyList.AdjacencyList(10)
am = AdjacencyMatrix.AdjacencyMatrix(10)

al.remove_edge(2, 3)

al.add_edge(0, 1)
al.add_edge(1, 2)
al.add_edge(2, 3)
al.add_edge(3, 0)
al.add_edge(0, 2)
'''
print(al.has_edge(0, 1)) # True
print(al.has_edge(1, 3)) # False

print(al.in_edges(2)) # It should return 0, 1 in any order.
print(al.out_edges(0)) # It should return 1, 2 in any order.
'''
# al.bfs(0) # The output mustbe 0,1,2,3 or 0,2,1,3
# al.dfs(0) # The output mustbe 0,2,3,1 or 0,1,2,3.
# al.r_dfs(1)

print(al.distance(0, 1))

'''

'''