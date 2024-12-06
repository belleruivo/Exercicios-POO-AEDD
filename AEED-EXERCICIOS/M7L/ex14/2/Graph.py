from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Grafo não-direcionado

    # Função utilizada pelo DFS
    def DFSUtil(self, vertex, visited, tree):
        visited.add(vertex)
        for neighbor in sorted(self.graph[vertex]):
            if neighbor not in visited:
                tree.append((vertex, neighbor))
                self.DFSUtil(neighbor, visited, tree)

    # Função para criar árvore geradora mínima usando DFS
    def DFS(self, start):
        visited = set()
        tree = []
        self.DFSUtil(start, visited, tree)
        return tree
