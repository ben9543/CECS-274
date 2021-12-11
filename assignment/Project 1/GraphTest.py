import AdjacencyList
import AdjacencyMatrix

al = AdjacencyList.AdjacencyList(10)
am = AdjacencyMatrix.AdjacencyMatrix(10)

al.add_edge(1, 2)
al.add_edge(2, 3)
al.add_edge(3, 0)

al.add_edge(0, 1)
al.add_edge(0, 2)
al.add_edge(0, 3)
al.add_edge(0, 4)

am.add_edge(0, 1)
am.add_edge(0, 2)
am.add_edge(0, 3)
am.add_edge(1, 4)
am.add_edge(2, 4)
am.add_edge(3, 5)
am.add_edge(4, 5)

print(am.in_edges(5))
print(am.out_edges(0))

