from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Grafo não-direcionado

    # Função para criar árvore geradora mínima usando BFS
    def BFS(self, start):
        visited = {key: False for key in self.graph}
        queue = deque([start])
        visited[start] = True
        tree = []

        while queue:
            vertex = queue.popleft()
            for neighbor in sorted(self.graph[vertex]):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    tree.append((vertex, neighbor))
        
        return tree
