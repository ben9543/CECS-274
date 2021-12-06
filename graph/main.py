
def create_adj_list(edges):
    di = {}
    for i in edges:
        if i[0] in di:
            di[i[0]].append(i[1])
        else:
            di[i[0]] = [i[1]]
        if i[1] in di:
            di[i[1]].append(i[0])
        else:
            di[i[1]] = [i[0]]
    return di

def hasPath(adj_list, source, target):
    stack = []
    stack.append(source)
    visited = set()
    while stack:
        x = stack.pop()
        if x not in visited:
            visited.add(x)
            if target in adj_list[x]:
                return True
            else:
                for child in adj_list[x]:
                    stack.append(child)
    return False

def shortestPath(adj_list, start, end):
    visited = set()
    queue = [[start, 0]]
    while queue:
        [node, dist] = queue.pop(0)
        if node == end:
            return [node, dist]
        else:
            for i in adj_list[node]:
                if i not in visited:
                    queue.append([i,dist+1])
        return False

def largest_components(adj_list):
    largest = []
    for node in adj_list:
        stack = [node]
        visited = list()
        while stack:
            x = stack.pop()
            if x not in visited:
                for child in adj_list[x]:
                    stack.append(child)
                visited.append(x)
            else:
                if len(largest) < len(visited):
                    largest = visited
    return largest

edges = [
    ('a', 'b'),
    ('a', 'c'),
    ('c', 'd'),
    ('d', 'e')
]

ad = create_adj_list(edges)
print(hasPath(ad, 'a', 'e'))

graph = {0:[8,1,5,6],1:[0],5:[0,8],8:[0,5],2:[3,4],3:[2,4],4:[3,2],6:[0]}
largest = largest_components(graph)
print(largest)
'''
# 
# Largest component = [0,1,6,5,8]
# Number of components = 2 ([0,1,5,6,8], [2,3,4])
'''