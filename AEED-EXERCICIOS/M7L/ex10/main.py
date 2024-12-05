# Escreva um programa que encontre o caminho mais curto a partir de A a todos os
# outros vértices do grafo abaixo. Encontre o caminho de custo mínimo a partir de B a
# todos os outros vértices.

import heapq

def dijkstra(grafo, inicio):
    distancias = {vertice: float('infinity') for vertice in grafo}
    # A distância até o próprio vértice de início é zero
    distancias[inicio] = 0
    # Usaremos uma fila de prioridade para processar os vértices
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)
        
        # Ignorar entradas na fila que já foram processadas
        if distancia_atual > distancias[vertice_atual]:
            continue
        
        # Verificar os vizinhos
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            # Atualizar a distância se encontrarmos um caminho mais curto
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))
    
    return distancias

grafo = {
    'A': {'B': 5, 'D': 2},
    'B': {'C': 2, 'E': 3},
    'C': {'E': 7},
    'D': {'C': 6, 'F': 8},
    'E': {'F': 1, 'G': 1},
    'F': {},
    'G': {}
}

# Encontrar o caminho mais curto a partir de 'A'
print("Distâncias a partir de A:", dijkstra(grafo, 'A'))

# Encontrar o caminho mais curto a partir de 'B'
print("Distâncias a partir de B:", dijkstra(grafo, 'B'))
