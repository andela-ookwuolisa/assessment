def dfs(graph,vertex, path=[]):
    path += [vertex]

    for neighbour in graph[vertex]:
        if neighbour not in path:
            path = dfs(graph, neighbour, path)
    return path

# sample graph 
# for this to work, the graph has to be sorted. i.e, 
# smaller number on the left, and biger number on the right
G = {1: [2, 3], 
     2: [4, 5],
     3: [5],
     4: [6],
     5: [6],
     6: [7],
     7: []}
print(dfs(G,1))

# G = {'A': ['B', 'C'],
#      'B': ['A', 'D', 'E'],
#      'C': ['A', 'F'],
#      'D': ['B'],
#      'E': ['B', 'F'],
#      'F': ['C', 'E']}
