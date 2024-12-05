# Dado os grafos abaixo, crie um programa que mostre o resultado da busca em
# largura e em profundidade começando do vértice 1.

from collections import defaultdict, deque

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)

    def bfs(self, inicio):
        visitados = set()
        fila = deque([inicio])
        resultado_bfs = []

        while fila:
            vertice = fila.popleft()
            if vertice not in visitados:
                visitados.add(vertice)
                resultado_bfs.append(vertice)
                fila.extend(self.grafo[vertice])

        return resultado_bfs

    def dfs(self, inicio):
        visitados = set()
        resultado_dfs = []

        def dfs_recursivo(vertice):
            if vertice not in visitados:
                visitados.add(vertice)
                resultado_dfs.append(vertice)
                for vizinho in self.grafo[vertice]:
                    dfs_recursivo(vizinho)

        dfs_recursivo(inicio)
        return resultado_dfs


# Criando os grafos representados na imagem
g1 = Grafo()
arestas_g1 = [
    (1, 2), (1, 3), (1, 7), (2, 4), (2, 5), (3, 6), (5, 6), (5, 7)
]
for u, v in arestas_g1:
    g1.adicionar_aresta(u, v)
    g1.adicionar_aresta(v, u)  # Grafo não direcionado

g2 = Grafo()
arestas_g2 = [
    (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (5, 7), (6, 8)
]
for u, v in arestas_g2:
    g2.adicionar_aresta(u, v)
    g2.adicionar_aresta(v, u)  # Grafo não direcionado

# Realizando as buscas para o Grafo 1
print("Grafo 1:")
print("BFS (a partir do vértice 1):", g1.bfs(1))
print("DFS (a partir do vértice 1):", g1.dfs(1))

# Realizando as buscas para o Grafo 2
print("\nGrafo 2:")
print("BFS (a partir do vértice 1):", g2.bfs(1))
print("DFS (a partir do vértice 1):", g2.dfs(1))
