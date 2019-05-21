def dfs(graph,vertex, path=[]):
    path += [vertex]

    for neighbour in graph[vertex]:
        if neighbour not in path:
            path = dfs(graph, neighbour, path)
    return path

# sample graph
G = {1: [2, 3], 
     2: [4, 5],
     3: [5],
     4: [6],
     5: [6],
     6: [7],
     7: []}
print(dfs(G,'A'))

# G = {'A': ['B', 'C'],
#      'B': ['A', 'D', 'E'],
#      'C': ['A', 'F'],
#      'D': ['B'],
#      'E': ['B', 'F'],
#      'F': ['C', 'E']}
