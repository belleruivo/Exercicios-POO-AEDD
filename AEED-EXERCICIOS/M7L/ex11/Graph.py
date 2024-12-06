from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Adicionando esta linha para garantir que o grafo seja não-direcionado

    def BFS(self, s):
        visited = {key: False for key in self.graph}
        queue = []
        
        queue.append(s)
        visited[s] = True
        
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
