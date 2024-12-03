'''1. Escreva um programa que, dados uma matriz de adjacência e dois nós de um grafo,
calcule:
a. O número de caminhos de determinado comprimento existentes entre eles.
b. O número total de caminhos existentes entre eles.'''

import numpy as np

def caminhos_comprimento_k(matriz_adj, origem, destino, k):
    """
    Calcula o número de caminhos de comprimento k entre dois nós.

    Args:
        matriz_adj (numpy.ndarray): Matriz de adjacência do grafo.
        origem (int): Nó de origem.
        destino (int): Nó de destino.
        k (int): Comprimento do caminho.

    Returns:
        int: Número de caminhos de comprimento k entre origem e destino.
    """
    matriz_potencia = np.linalg.matrix_power(matriz_adj, k)
    return matriz_potencia[origem, destino]

def total_caminhos(matriz_adj, origem, destino, max_comprimento=None):
    """
    Calcula o número total de caminhos entre dois nós.

    Args:
        matriz_adj (numpy.ndarray): Matriz de adjacência do grafo.
        origem (int): Nó de origem.
        destino (int): Nó de destino.
        max_comprimento (int, opcional): Limite superior para o comprimento dos caminhos.
                                        Se None, calcula infinitamente.

    Returns:
        int: Número total de caminhos entre origem e destino.
    """
    if max_comprimento is not None:
        total = 0
        for k in range(1, max_comprimento + 1):
            total += caminhos_comprimento_k(matriz_adj, origem, destino, k)
        return total
    else:
        # Para caminhos infinitos, usamos a fórmula da soma geométrica
        identidade = np.eye(len(matriz_adj))
        try:
            inversa = np.linalg.inv(identidade - matriz_adj)
            soma_infinita = inversa - identidade
            return int(soma_infinita[origem, destino])
        except np.linalg.LinAlgError:
            raise ValueError("A matriz não converge para caminhos infinitos.")

# Exemplo de uso
matriz_adjacencia = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
])

origem = 0
destino = 2
k = 3

print(f"Número de caminhos de comprimento {k} entre {origem} e {destino}:",
      caminhos_comprimento_k(matriz_adjacencia, origem, destino, k))

max_comprimento = 5
print(f"Número total de caminhos até comprimento {max_comprimento} entre {origem} e {destino}:",
      total_caminhos(matriz_adjacencia, origem, destino, max_comprimento))
