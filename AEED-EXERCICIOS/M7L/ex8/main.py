# 8. Crie um programa que ache a Arvore Geradora Mínima do grafo abaixo utilizando o
# Algoritmo de Prim começando do vértice A.

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

# Executando o algoritmo de Prim
mst, total_cost = prim_algorithm(graph, start_vertex)

print("Árvore Geradora Mínima (Prim):")
for edge in mst:
    print(f"Vértices: {chr(edge[0] + 65)} - {chr(edge[1] + 65)}, Peso: {edge[2]}")

print(f"Custo total da AGM: {total_cost}")
