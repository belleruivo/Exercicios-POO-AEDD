# Crie um programa que ache a Arvore Geradora Mínima do grafo abaixo utilizando o
# Algoritmo de Prim começando do vértice A.
# A árvore geradora mínima é uma árvore que conecta todos os vértices do grafo com o menor custo total possível, ou seja, 
# o total das arestas que a compõem deve ser minimizado.


import heapq

def algoritmo_prim(grafo, inicio):
    num_vertices = len(grafo) #A
    visitado = [False] * num_vertices  
    heap_minimo = [(0, inicio)]  # armazenamento das arestas 
    agm = []  # Armazenamento da Árvore Geradora Mínima
    custo_total = 0

    while heap_minimo:
        peso, vertice_atual = heapq.heappop(heap_minimo) #remove e retorna o elemento

        if visitado[vertice_atual]:
            continue

        visitado[vertice_atual] = True
        custo_total += peso

        for vizinho in range(num_vertices):
            if grafo[vertice_atual][vizinho] != 0 and not visitado[vizinho]:
                heapq.heappush(heap_minimo, (grafo[vertice_atual][vizinho], vizinho))
                agm.append((vertice_atual, vizinho, grafo[vertice_atual][vizinho]))

    return agm, custo_total

grafo = [
    [0, 15, 10, 19, 0, 0, 0, 0, 0, 0],  # A
    [15, 0, 0, 7, 17, 0, 0, 0, 0, 0],   # B
    [10, 0, 0, 16, 0, 14, 0, 0, 0, 0],  # C
    [19, 7, 16, 0, 12, 6, 3, 0, 0, 0],  # D
    [0, 17, 0, 12, 0, 0, 20, 13, 0, 0], # E
    [0, 0, 14, 6, 0, 0, 9, 0, 5, 0],    # F
    [0, 0, 0, 3, 20, 9, 0, 4, 1, 11],  # G
    [0, 0, 0, 0, 13, 0, 4, 0, 0, 2],   # H
    [0, 0, 0, 0, 0, 5, 1, 0, 0, 18],  # I
    [0, 0, 0, 0, 0, 0, 11, 2, 18, 0]   # J
]

vertice_inicial = 0

def agm_prim(grafo, inicio):
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
    
        arestas.remove(min_aresta)

        # Processa a aresta de menor peso
        peso, u, v = min_aresta
        if not visitado[v]:
            visitado[v] = True
            agm.append((u, v, peso))
            
        for w in range(n):
            if grafo[v][w] != 0 and not visitado[w]:
                arestas.append((grafo[v][w], v, w))

        arestas.sort()  # Reordena as arestas por peso

    return agm


agm = agm_prim(grafo, 0)

print("Arestas da Árvore Geradora Mínima:")
for u, v, peso in agm:
    print(f"{chr(u + 65)} - {chr(v + 65)} (peso: {peso})")
