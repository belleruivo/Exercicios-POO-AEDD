'''1. Escreva um programa que, dados uma matriz de adjacência e dois nós de um grafo,
calcule:
a. O número de caminhos de determinado comprimento existentes entre eles.
b. O número total de caminhos existentes entre eles.'''

import numpy as np

def caminhos_por_comprimento(matriz, no_inicio, no_fim, comprimento):
    """
    Calcula o número de caminhos de determinado comprimento entre dois nós.
    """
    matriz_potencia = np.linalg.matrix_power(matriz, comprimento)
    return matriz_potencia[no_inicio][no_fim]

def todos_os_caminhos(matriz, no_inicio, no_fim, max_comprimento=3):
    """
    Calcula o número total de caminhos entre dois nós até um comprimento máximo.
    """
    total_caminhos = 0
    for comprimento in range(1, max_comprimento + 1):
        total_caminhos += caminhos_por_comprimento(matriz, no_inicio, no_fim, comprimento)
    return total_caminhos

# Exemplo simples de grafo
matriz_adjacencia = np.array([
    [0, 1, 0],  # Nó 0 -> Nó 1
    [1, 0, 1],  # Nó 1 -> Nó 0 e Nó 2
    [0, 1, 0]   # Nó 2 -> Nó 1
])

no_inicio = 0
no_fim = 2
comprimento = 2

# Apresentação rápida
print(f"Número de caminhos de comprimento {comprimento} entre os nós {no_inicio} e {no_fim}:",
      caminhos_por_comprimento(matriz_adjacencia, no_inicio, no_fim, comprimento))

print(f"Número total de caminhos entre os nós {no_inicio} e {no_fim}:",
      todos_os_caminhos(matriz_adjacencia, no_inicio, no_fim))


