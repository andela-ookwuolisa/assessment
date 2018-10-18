from collections import defaultdict 

class Graph():
  def __init__(self):
    self.graph = defaultdict(list)
    self.edges = list()

  def addEdge(self,u,v):
    self.graph[u].append(v) 

  def generate_edges(self):
      for node in self.graph:
          for neighbour in self.graph[node]:
              self.edges.append((node, neighbour))
      return self.edges

  def generate_vertices(self):
    return list(self.graph.keys())

  
graph = Graph()

graph.addEdge('a','c') 
graph.addEdge('b','c') 
graph.addEdge('b','e') 
graph.addEdge('c','d') 
graph.addEdge('c','e') 
graph.addEdge('c','a') 
graph.addEdge('c','b') 
graph.addEdge('e','b') 
graph.addEdge('d','c') 
graph.addEdge('e','c')

print("Edges")
print(graph.generate_edges()) 
print("Vertices") 
print(graph.generate_vertices())
