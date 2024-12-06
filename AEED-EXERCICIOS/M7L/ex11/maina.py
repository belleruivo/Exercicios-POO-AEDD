# 8. Crie um programa que ache a Arvore Geradora Mínima do grafo abaixo utilizando o
# Algoritmo de Prim começando do vértice A.

<<<<<<< HEAD
import heapq

def prim_algorithm(graph, start):
    num_vertices = len(graph)
    visited = [False] * num_vertices  # Para rastrear vértices visitados
    min_heap = [(0, start)]  # (peso, vértice)
    mst = []  # Armazenamento da Árvore Geradora Mínima
    total_cost = 0

    while min_heap:
        weight, current_vertex = heapq.heappop(min_heap)

        if visited[current_vertex]:
            continue

        visited[current_vertex] = True
        total_cost += weight

        for neighbor in range(num_vertices):
            if graph[current_vertex][neighbor] != 0 and not visited[neighbor]:
                heapq.heappush(min_heap, (graph[current_vertex][neighbor], neighbor))
                mst.append((current_vertex, neighbor, graph[current_vertex][neighbor]))

    return mst, total_cost

graph = [
    [0, 15, 10, 19, 0, 0, 0, 0, 0, 0], # A
     [15, 0, 0, 7, 17, 0, 0, 0, 0, 0],  # B
     [10, 0, 0, 16, 0, 14, 0, 0, 0, 0],  # C
     [19, 7, 16, 0, 12, 6, 3, 0, 0, 0], # D
     [0, 17, 0, 12, 0, 0, 20, 13, 0, 0],# E
     [0, 0, 14, 6, 0, 0, 9, 0, 5, 0],  # F
     [0, 0, 0, 3, 20, 9, 0, 4, 1, 11],  # G
     [0, 0, 0, 0, 13, 0, 4, 0, 0, 2],    # H
     [0, 0, 0, 0, 0, 5, 1, 0, 0, 18],   # I
     [0, 0, 0, 0, 0, 0, 11, 2, 18, 0]    # J
]


# Índice inicial (A = 0)
start_vertex = 0
=======
# A árvore geradora mínima é uma árvore que conecta todos os vértices do grafo com o menor custo total possível, ou seja, 
# o total das arestas que a compõem deve ser minimizado.

def prim_agm(grafo, inicio):
    n = len(grafo)
    visitado = [False] * n  # Lista para verificar se o vértice foi visitado
    agm = []  # Lista para armazenar as arestas da Árvore Geradora Mínima
    
    visitado[inicio] = True
    
    # Lista de arestas que podem ser adicionadas, armazenadas como (peso, u, v)
    arestas = []
    for v in range(n):
        if grafo[inicio][v] != 0:  # Adiciona arestas conectadas ao vértice inicial
            arestas.append((grafo[inicio][v], inicio, v))

    arestas.sort()  # Ordena as arestas por peso

    while arestas:
        min_peso = float('inf')
        min_aresta = None
        
        for aresta in arestas:
            if aresta[0] < min_peso:  # Aresta com menor peso
                min_peso = aresta[0]
                min_aresta = aresta
        
        # Remove a aresta selecionada manualmente
        arestas.remove(min_aresta)

        # Passo 2: Processa a aresta de menor peso
        peso, u, v = min_aresta
        if not visitado[v]:
            visitado[v] = True
            agm.append((u, v, peso))
>>>>>>> 86fbd5c24781141b46ed8cd74ceab322adf04f5a

            # Adiciona novas arestas conectadas ao vértice v
            for w in range(n):
                if grafo[v][w] != 0 and not visitado[w]:
                    arestas.append((grafo[v][w], v, w))

            arestas.sort()  # Reordena as arestas por peso

    return agm

grafo = [
    [0, 15, 10, 19, 0, 0, 0, 0, 0, 0],
    [15, 0, 0, 7, 17, 0, 0, 0, 0, 0],
    [10, 0, 0, 16, 14, 0, 0, 0, 0, 0],
    [19, 7, 16, 0, 12, 13, 3, 0, 0, 0],
    [0, 17, 14, 12, 0, 20, 13, 0, 0, 0],
    [0, 0, 0, 13, 20, 0, 9, 5, 0, 0],
    [0, 0, 0, 3, 13, 9, 0, 4, 1, 11],
    [0, 0, 0, 0, 0, 5, 4, 0, 0, 18],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 18],
    [0, 0, 0, 0, 0, 0, 11, 18, 18, 0]
]

# Chamando a função com o vértice inicial 'A' (índice 0)
agm = prim_agm(grafo, 0)

print("Arestas da Arvore Geradora Minima:")
for u, v, peso in agm:
    print(f"{chr(u + 65)} - {chr(v + 65)} (peso: {peso})")
