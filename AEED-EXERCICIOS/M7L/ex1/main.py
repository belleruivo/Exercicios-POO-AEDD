'''1. Escreva um programa que, dados uma matriz de adjacência e dois nós de um grafo,
calcule:
a. O número de caminhos de determinado comprimento existentes entre eles.
b. O número total de caminhos existentes entre eles.'''

def multiplica_matrizes(matriz_a, matriz_b):
    """
    Multiplica duas matrizes quadradas.
    """
    n = len(matriz_a)
    resultado = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]
    return resultado

def eleva_matriz(matriz, k):
    """
    Eleva uma matriz quadrada à potência k.
    """
    n = len(matriz)
    resultado = [[1 if i == j else 0 for j in range(n)] for i in range(n)]  # Matriz identidade
    matriz_base = matriz
    for _ in range(k):
        resultado = multiplica_matrizes(resultado, matriz_base)
    return resultado


def caminhos_comprimento_k(matriz_adj, origem, destino, k):
    """
    Calcula o número de caminhos de comprimento k entre dois nós.
    """
    matriz_potencia = eleva_matriz(matriz_adj, k)
    return matriz_potencia[origem][destino]


def total_caminhos(matriz_adj, origem, destino, max_comprimento=None):
    """
    Calcula o número total de caminhos entre dois nós.
    """
    n = len(matriz_adj)
    if max_comprimento is not None:
        total = 0
        for k in range(1, max_comprimento + 1):
            total += caminhos_comprimento_k(matriz_adj, origem, destino, k)
        return total
    else:
        raise NotImplementedError("Caminhos infinitos não estão implementados sem bibliotecas.")


# Exemplo de uso
matriz_adjacencia = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 1, 1, 0]
]

origem = 0
destino = 2
k = 3

print(f"Número de caminhos de comprimento {k} entre {origem} e {destino}:",
      caminhos_comprimento_k(matriz_adjacencia, origem, destino, k))

max_comprimento = 5
print(f"Número total de caminhos até comprimento {max_comprimento} entre {origem} e {destino}:",
      total_caminhos(matriz_adjacencia, origem, destino, max_comprimento))
