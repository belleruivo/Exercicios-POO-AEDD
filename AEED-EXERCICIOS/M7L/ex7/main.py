# Encontre a árvore geradora mínima do seguinte grafo (pesquise):
# a. Usando o algoritmo de Krukal.
# O algoritmo de Kruskal é usado para encontrar a Árvore Geradora Mínima (AGM) de um grafo. 
# Ele funciona selecionando as arestas de menor peso e adicionando-as ao conjunto da árvore geradora, 
# desde que não formem ciclos. A seguir, apresento a implementação do algoritmo de Kruskal em Python:

# Classe para representar uma aresta
class Aresta:
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = []

    def adicionar_aresta(self, u, v, peso):
        self.arestas.append(Aresta(u, v, peso))

    # Função para encontrar o conjunto de um vértice (com compressão de caminho)
    def encontrar_conjunto(self, pai, vertice):
        if pai[vertice] != vertice:
            pai[vertice] = self.encontrar_conjunto(pai, pai[vertice])
        return pai[vertice]

    # Função para unir dois conjuntos (usando rank para otimização)
    def unir_conjuntos(self, pai, rank, u, v):
        raiz_u = self.encontrar_conjunto(pai, u)
        raiz_v = self.encontrar_conjunto(pai, v)

        if rank[raiz_u] < rank[raiz_v]:
            pai[raiz_u] = raiz_v
        elif rank[raiz_u] > rank[raiz_v]:
            pai[raiz_v] = raiz_u
        else:
            pai[raiz_v] = raiz_u
            rank[raiz_u] += 1

    def kruskal(self):
        self.arestas.sort(key=lambda aresta: aresta.peso)

        pai = {}
        rank = {}
        agm = []
        custo_total = 0

        for vertice in self.vertices:
            pai[vertice] = vertice
            rank[vertice] = 0

        for aresta in self.arestas:
            u, v, peso = aresta.u, aresta.v, aresta.peso
            if self.encontrar_conjunto(pai, u) != self.encontrar_conjunto(pai, v):
                agm.append((u, v, peso))
                custo_total += peso
                self.unir_conjuntos(pai, rank, u, v)

        return agm, custo_total


vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
arestas = [
    ('a', 'b', 4), ('a', 'h', 8), ('b', 'c', 8), ('b', 'h', 11),
    ('c', 'd', 7), ('c', 'f', 4), ('c', 'i', 2), ('d', 'e', 9),
    ('d', 'f', 14), ('e', 'f', 10), ('f', 'g', 2), ('g', 'h', 1),
    ('g', 'i', 6), ('h', 'i', 7)
]

g = Grafo(vertices)
for u, v, peso in arestas:
    g.adicionar_aresta(u, v, peso)

agm, custo_total = g.kruskal()

print("Árvore Geradora Mínima (AGM) usando o algoritmo de Kruskal:")
for u, v, peso in agm:
    print(f"Aresta {u} - {v} com peso {peso}")
print(f"Custo total da AGM: {custo_total}")



# b. Usando o algoritmo de Prim, começando a partir do vértice a.
import heapq

class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_aresta(self, u, v, peso):
        if u not in self.grafo:
            self.grafo[u] = []
        if v not in self.grafo:
            self.grafo[v] = []
        self.grafo[u].append((peso, v))
        self.grafo[v].append((peso, u))  # Grafo não direcionado

    def prim(self, inicio):
        visitados = set()
        fila_prioridade = []
        agm = []
        custo_total = 0

        # Adicionar as arestas do vértice inicial na fila de prioridade
        visitados.add(inicio)
        for aresta in self.grafo[inicio]:
            heapq.heappush(fila_prioridade, aresta)

        while fila_prioridade:
            peso, vertice = heapq.heappop(fila_prioridade)
            if vertice not in visitados:
                visitados.add(vertice)
                agm.append((peso, vertice))
                custo_total += peso

                for aresta in self.grafo[vertice]:
                    if aresta[1] not in visitados:
                        heapq.heappush(fila_prioridade, aresta)

        return agm, custo_total

g = Grafo()
arestas = [
    ('a', 'b', 4), ('a', 'h', 8), ('b', 'c', 8), ('b', 'h', 11),
    ('c', 'd', 7), ('c', 'f', 4), ('c', 'i', 2), ('d', 'e', 9),
    ('d', 'f', 14), ('e', 'f', 10), ('f', 'g', 2), ('g', 'h', 1),
    ('g', 'i', 6), ('h', 'i', 7)
]

for u, v, peso in arestas:
    g.adicionar_aresta(u, v, peso)

agm, custo_total = g.prim('a')

print("Árvore Geradora Mínima (AGM) usando o algoritmo de Prim:")
for peso, vertice in agm:
    print(f"Aresta com peso {peso} conectando ao vértice {vertice}")
print(f"Custo total da AGM: {custo_total}")
