def bfs(graph, start):
    explored, queue = set(), [start]
    explored.add(start)
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                queue.append(w)
    return explored



# sample graph
G = {1: [2, 3], 
     2: [4, 5],
     3: [5],
     4: [6],
     5: [6],
     6: [7],
     7: []}

print(bfs(G,1))

# G = {'A': ['B', 'C'],
#      'B': ['A', 'D', 'E'],
#      'C': ['A', 'F'],
#      'D': ['B'],
#      'E': ['B', 'F'],
#      'F': ['C', 'E']}
