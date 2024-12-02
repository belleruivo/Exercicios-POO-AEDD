'''1. Escreva um programa que, dados uma matriz de adjacência e dois nós de um grafo,
calcule:
a. O número de caminhos de determinado comprimento existentes entre eles.
b. O número total de caminhos existentes entre eles.'''

import numpy as np

def caminho_comprimento(matriz_adjacencia, origem, destino, comprimento):
    """
    Calcula o número de caminhos de comprimento específico entre dois nós
    usando multiplicação de matrizes (exponenciação de matrizes).
    """
    n = len(matriz_adjacencia)
    
    # Matriz adjacente elevada ao comprimento especificado
    matriz_potencia = np.linalg.matrix_power(matriz_adjacencia, comprimento)
    
    # O número de caminhos de comprimento específico entre origem e destino
    return matriz_potencia[origem][destino]

def caminho_total(matriz_adjacencia, origem, destino):
    """
    Calcula o número total de caminhos entre dois nós, somando
    as potências das matrizes de adjacência de 1 até n.
    """
    n = len(matriz_adjacencia)
    caminho_total = 0
    
    # Iterando sobre potências da matriz de adjacência
    for i in range(1, n+1):
        matriz_potencia = np.linalg.matrix_power(matriz_adjacencia, i)
        caminho_total += matriz_potencia[origem][destino]
    
    return caminho_total

# Exemplo de uso
def main():
    # Matriz de adjacência de exemplo
    matriz_adjacencia = np.array([
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ])
    
    origem = 0  # Nó de origem
    destino = 2  # Nó de destino
    comprimento = 2  # Comprimento do caminho

    # Número de caminhos de comprimento específico
    caminhos_comprimento = caminho_comprimento(matriz_adjacencia, origem, destino, comprimento)
    print(f"Número de caminhos de comprimento {comprimento} entre {origem} e {destino}: {caminhos_comprimento}")
    
    # Número total de caminhos
    caminhos_totais = caminho_total(matriz_adjacencia, origem, destino)
    print(f"Número total de caminhos entre {origem} e {destino}: {caminhos_totais}")

main()